from django import forms
from django.forms import ModelForm


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
