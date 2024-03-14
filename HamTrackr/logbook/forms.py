from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    frequency = forms.DecimalField(label='Frequency (kHz)')  # Modify the label

    class Meta:
        model = Contact
        fields = ['callsign', 'frequency', 'mode']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Real email address is required!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
