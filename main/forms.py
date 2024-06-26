from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from main.models import *
# register/create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
# Login a user
class LoginForms(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#Adding new record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email', 'phone', 'address','city', 'state', 'country']
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email', 'phone', 'address','city', 'state', 'country']
        
class ViewForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'