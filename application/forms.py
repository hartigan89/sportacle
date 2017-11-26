from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(
            attrs = {
                'class':'form-control'
            }
        ))   
    
    username = forms.CharField(widget=forms.TextInput(
            attrs = {
                'class':'form-control'
            }
        ))
    
    password = forms.CharField(widget=forms.PasswordInput(
            attrs = {
                'class':'form-control'
            }
        ))
        
    password_repeat = forms.CharField(label='Retype Password', widget=forms.PasswordInput(
            attrs = {
                'class':'form-control'
            }
        ))
    
    class Meta():
        model = User
        fields = ('email', 'username', 'password',)
        