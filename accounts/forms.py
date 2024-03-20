import string
from django import forms
from .models import Reservation
from django.core.validators import RegexValidator
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # Import the CustomUser model

class ProfileForm(forms.ModelForm):
    phone = forms.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    class Meta:
        model = CustomUser  # Use CustomUser instead of Profile
        fields = ['phone']

    # def clean_bio(self):
    #     bio = self.cleaned_data.get('bio')
    #     if 'badword' in bio:
    #         raise ValidationError("Please do not use bad words in your bio.")
    #     return bio

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['car', 'start_date', 'end_date',]

def validate_no_special_characters(value):
    if any(char not in string.ascii_letters + string.digits for char in value):
        raise ValidationError("Special characters are not allowed.")

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(
        max_length=CustomUser._meta.get_field('username').max_length,  # Use CustomUser's username field length
        help_text="Username must not contain special characters!",
        validators=[validate_no_special_characters]
    )

    class Meta:
        model = CustomUser  # Use CustomUser instead of Profile
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
