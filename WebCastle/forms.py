from django import forms

from .models import User


# class RegisterForm(forms.Form):
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'نام کاربری', 'required': 'True'}),
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل', 'required': 'True'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'required': 'True'}),
        }

    repassword = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
        attrs={'placeholder': 'تکرار رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))

    # username = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                            widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    # email = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                         widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    # password = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                            widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
