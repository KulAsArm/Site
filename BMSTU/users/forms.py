from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "field_item",
                "placeholder": 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': "field_item",
                "placeholder": 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", 'email']

        widgets = {
            "username": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите имя пользоваетля'
            }),
            "first_name": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите имя'
            }),
            "last_name": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите фамилию'
            }),
            "email": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите email'
            }),
        }

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(UserRegisterForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['style'] = 'border-radius: 10px'
#         self.fields['email'].widget.attrs['style'] = 'border-radius: 10px'
#         self.fields['password1'].widget.attrs['style'] = 'border-radius: 10px'
#         self.fields['password2'].widget.attrs['style'] = 'border-radius: 10px'

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={ 'class': "field_item",   "placeholder": 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': "field_item",
                "placeholder": 'Пароль'}), label='Пароль')


