from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    user = forms.CharField(label='', max_length=100, help_text='',
                           widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    username = forms.CharField(label='', required=True, max_length=100, help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.CharField(label='', required=True, max_length=100, help_text='',
                            widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(label='', required=True, max_length=100, help_text='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    repassword = forms.CharField(label='', required=True, max_length=100, help_text='',
                                 widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))
