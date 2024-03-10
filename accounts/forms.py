from django import forms
from .models import Profile, Reservation
from django.core.validators import RegexValidator
from django.forms import ValidationError


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
