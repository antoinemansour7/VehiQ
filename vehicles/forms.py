
from django.utils import timezone
from django import forms
from .models import Car


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price', 'mileage', 'image', ]

    def __init__(self, *args, **kwargs):
        super(AddCarForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = True
        self.fields['mileage'].required = True

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = timezone.now().year

        if year > current_year:
            raise forms.ValidationError("Invalid year. Please enter a valid year.")

        return year

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")

        return price

    def clean_mileage(self):
        mileage = self.cleaned_data['mileage']

        if mileage < 0:
            raise forms.ValidationError("Mileage cannot be negative.")

        return mileage


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price', 'mileage', 'image', ]

    def __init__(self, *args, **kwargs):
        super(EditCarForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = True
        self.fields['mileage'].required = True

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = timezone.now().year

        if year > current_year:
            raise forms.ValidationError("Invalid year. Please enter a valid year.")

        return year

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")

        return price

    def clean_mileage(self):
        mileage = self.cleaned_data['mileage']

        if mileage < 0:
            raise forms.ValidationError("Mileage cannot be negative.")

        return mileage
