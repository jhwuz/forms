from django import forms
from django.forms import ModelForm
from .models import Post


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        exclude = ['author']
