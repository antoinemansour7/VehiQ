import string
from django import forms
from .models import Profile, Reservation
from django.core.validators import RegexValidator
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    phone = forms.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    
    class Meta:
        model = Profile
        fields = ['bio', 'phone']

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if 'badword' in bio:
            raise ValidationError("Please do not use bad words in your bio.")
        return bio
    
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['car', 'start_date', 'end_date',] 


def validate_no_special_characters(value):
    if any(char not in string.ascii_letters + string.digits for char in value):
        raise ValidationError("Special characters are not allowed.")

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=Profile.USER_TYPE_CHOICES, widget=forms.RadioSelect)
    username = forms.CharField(
        max_length=Profile._meta.get_field('user').max_length,
        help_text="Username must not contain special characters!",
        validators=[validate_no_special_characters]
    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.email = self.cleaned_data['email']
        profile.save()

        user_type = self.cleaned_data['user_type']
        profile.user_type = user_type
        if commit:
            profile.save()

        return profile