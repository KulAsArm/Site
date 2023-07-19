from django import forms
from django.contrib.auth.models import User
from .models import Student


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


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={ 'class': "field_item",   "placeholder": 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': "field_item",
                "placeholder": 'Пароль'}), label='Пароль')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['FIO', 'email', 'phone', 'group', 'names_of_priority', 'telegram']

        widgets = {
            "FIO": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Иванов Иван Иванович'
            }),
            "email": forms.EmailInput(attrs={
                'class': "field_item",
                "placeholder": 'email@mail.ru'
            }),
            "phone": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": '+79953422112'
            }),
            "group": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'РК9-63Б'
            }),
            "names_of_priority": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите льготы'
            }),
            "telegram": forms.TextInput(attrs={
                'class': "field_item",
                "placeholder": 'Введите telegram-аккаунт'
            }),

        }

