from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from . import models
from . models import *
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','isbn','author','category']
class UploadFileForm(forms.Form):
    file = forms.FileField()

class dashboardfom(forms.Form):
    text = forms.CharField(max_length=100,label="enter your search: ")