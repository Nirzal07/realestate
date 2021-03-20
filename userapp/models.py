from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from webapp.models import PropertyDetails
from daleyvai.settings import BASE_DIR

class ProfilePic(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture= models.ImageField(upload_to='profile_pictures', default=BASE_DIR/'media/profile.png')

    def __str__(self):
        return self.user.username


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ['profile_picture']

class UserRegisterationForm(forms.ModelForm):
    """custom user registration"""
    confirm_password= forms.PasswordInput()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    first_name= forms.CharField(label= 'First Name')
    last_name= forms.CharField(label= 'Last Name')

    class Meta:
        model= User
        fields= ['first_name', 'last_name']

class Favourites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    property = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)