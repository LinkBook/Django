from django import forms


class RegisterForm(forms.Form):
    user = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    username = forms.CharField(label='', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.CharField(label='', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(label='', required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    repassword = forms.CharField(label='', required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
