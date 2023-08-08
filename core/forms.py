from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AreaForm(forms.Form):
    OPTIONS = (
        ('bfa', 'Burkina Faso'),
        ('gmb', 'Gambia'),
        ('gha', 'Ghana'),
        ('gin', 'Guniea'),
        ('mli', 'Mali'),
        ('mrt', 'Mauritania'),
        ('ngr', 'Niger'),
        ('sen', 'Senegal'),
        ('tgo', 'Togo'),
    )

    country = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(
        attrs={'class': 'form-select'}))


class CropForm(forms.Form):
    OPTIONS = (
        ('cas', 'Cassava'),
        ('mil', 'Millet'),
        ('rce', 'Rice'),
        ('sor', 'Sorghum'),
        ('mze', 'Maize'),
        ('yam', 'Yams'),
        ('opm', 'Oil palm'),
    )
    Crop = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(
        attrs={'class': 'form-select'}))


class InputForm(forms.Form):
    Temperature = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Temperature'}))
    Precipitation = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Precipitation'}))
    Pesticides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesticides'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password': None,
            'password2': None
        }
