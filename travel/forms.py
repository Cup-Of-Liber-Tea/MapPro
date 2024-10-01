from django import forms
from .models import Tourist


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ['name', 'description', 'location', 'operating_hours', 'entrance_fee', 'images', 'parking']
