from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Profile

'''bu UserCreate formni qolda email qoshiib chiqan vationatimiz'''
class UserRegister(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']


class UpdateProfile(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateAvatar(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


