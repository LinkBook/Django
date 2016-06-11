from django import forms

from .models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Karbar
        fields = ('name', 'username', 'email', 'password', 'rep')

    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    username = forms.CharField(label='', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.CharField(label='', required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(label='', required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    rep = forms.CharField(label='', required=True,
                          widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'نام کامل'}))
    email = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    message = forms.CharField(label='',
                              widget=forms.TextInput(attrs={'placeholder': 'پیام ارسالی'}))

    # class RegisterForm(forms.Form):
    # class RegisterForm(forms.ModelForm):
    #     class Meta:
    #         model = User
    #         fields = ['username', 'email', 'password']
    #         widgets = {
    #             'username': forms.TextInput(attrs={'placeholder': 'نام کاربری', 'required': 'True'}),
    #             'email': forms.TextInput(attrs={'placeholder': 'ایمیل', 'required': 'True'}),
    #             'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'required': 'True'}),
    #         }

    repassword = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
        attrs={'placeholder': 'تکرار رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))


class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = ('username', 'password')

    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'رمز عبور'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_name', 'comment_email', 'comment')

    comment_name = forms.CharField(label='',
                                   widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    comment_email = forms.CharField(label='',
                                    widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    comment = forms.CharField(label='',
                              widget=forms.TextInput(attrs={'placeholder': 'کامنت'}))

    # username = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                            widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    # email = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                         widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    # password = forms.CharField(label='', required=True, max_length=100, help_text='',
    #                            widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
