from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile
import re

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=6, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label="Your password")
    password_confirm = forms.CharField(min_length=6,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                       label="Confirm password")
    faculty = forms.ChoiceField(required=True, choices=Profile.FACULTIES, label="Your faculty")
    phone_number = forms.CharField(widget=forms.TextInput, required=False, label="Your phone number")

    class Meta:
        model = User
        fields = ['faculty', 'phone_number','first_name',
                  'last_name', 'username', 'email',
                  'password', 'password_confirm']
        labels = {'first_name':'Your first name',
                  'last_name':'Your last name',
                  'username':'Your username',
                  'email':'Your e-mail adress '}
        help_texts = {'email':"Enter a e-mail which you're using it currently.",
                      'username':''}

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
            self.fields['faculty'].widget.attrs = {'class': 'form-control', 'label':'Fakülte:'}
            self.fields['phone_number'].widget.attrs = {'class': 'form-control', 'placeholder': '5xxxxxxxxx'}

class LoginForm(forms.Form):
    username = forms.CharField(label='Username or e-mail:', required=True, max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'your username or e-mail adress'}))

    password = forms.CharField(label='Password:', required=True, max_length=50,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'your password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
                raise forms.ValidationError('<b>This user does not exist or wrong information.</b>')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match(r"[^@]+@[^@]+\.[^@]+", username):
            users = User.objects.filter(email__iexact=username)
            print(users)
            if len(users) > 0 and len(users) == 1:
                return users.first().username
        return username

class UpdateForm(forms.ModelForm):
    faculty = forms.ChoiceField(required=True, choices=Profile.FACULTIES, label="Your faculty")
    phone_number = forms.CharField(widget=forms.TextInput, required=False, label="Your phone number")

    class Meta:
        model = User
        fields = ['faculty', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['faculty'].widget.attrs = {'class': 'form-control'}
        self.fields['phone_number'].widget.attrs = {'class': 'form-control', 'placeholder': '5xxxxxxxxx'}

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number', None)
        try:
            int(phone_number)
            if len(phone_number) != 10:
                raise forms.ValidationError("Max. 10 characters.")
        except ValueError:
            raise forms.ValidationError("This isn't a phone number.")
        return phone_number