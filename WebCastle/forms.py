from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

from .models import *

User = get_user_model()
Gr = Group()


class ReistrationForm(forms.ModelForm):
    password = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
        attrs={'placeholder': ' رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))
    repassword = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
        attrs={'placeholder': 'تکرار رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))

    class Meta:
        model = User
        fields = ['username', 'email', ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('repassword')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password do not match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        print
        user_count
        if user_count > 0 and email:
            raise forms.ValidationError("this email is signed up before")
        return email

    def add_to_default_group(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            group = Group.objects.get(name='Admin')
            user.groups.add(group)

    def save(self, commit=True):
        user = super(ReistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        post_save.connect(ReistrationForm.add_to_default_group, sender=User)
        Gr.group_id = 2
        if commit:
            user.save()
        return user

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'نام کاربری', 'required': 'True'}),
#             'email': forms.TextInput(attrs={'placeholder': 'ایمیل', 'required': 'True'}),
#             # 'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'required': 'True'}),
#         }
#
#     password = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
#         attrs={'placeholder': ' رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))
#     repassword = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
#         attrs={'placeholder': 'تکرار رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('repassword')
#         print("zzzz PassClen zzzzz")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("password do not match")
#         return password2
#
#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         user_count = User.objects.filter(email=email).count()
#         print(user_count)
#         print("zzzz EmailClen zzzzz")
#         if user_count > 0 and email:
#             raise forms.ValidationError("this email is signed up before")
#         return email
#
#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         print("zzzz save zzzzz")
#         if commit:
#             user.save()
#         return user

#
#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('name', 'email', 'message')
#
#     name = forms.CharField(label='',
#                            widget=forms.TextInput(attrs={'placeholder': 'نام کامل'}))
#     email = forms.CharField(label='',
#                             widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
#     message = forms.CharField(label='',
#                               widget=forms.TextInput(attrs={'placeholder': 'پیام ارسالی'}))
#
#     # class RegisterForm(forms.ModelForm):
#     #     class Meta:
#     #         model = User
#     #         fields = ['username', 'email', 'password']
#     #         widgets = {
#     #             'username': forms.TextInput(attrs={'placeholder': 'نام کاربری', 'required': 'True'}),
#     #             'email': forms.TextInput(attrs={'placeholder': 'ایمیل', 'required': 'True'}),
#     #             'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'required': 'True'}),
#     #         }
#
#     repassword = forms.CharField(label='', required=True, max_length=100, help_text='', widget=forms.PasswordInput(
#         attrs={'placeholder': 'تکرار رمز عبور', 'required': 'True', 'onkeyup': 'checkPass(); return false;'}))
#
#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ('comment_name', 'comment_email', 'comment')
#
#     comment_name = forms.CharField(label='',
#                                    widget=forms.TextInput(attrs={'placeholder': 'نام'}))
#     comment_email = forms.CharField(label='',
#                                     widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
#     comment = forms.CharField(label='',
#                               widget=forms.TextInput(attrs={'placeholder': 'کامنت'}))
#
#     # username = forms.CharField(label='', required=True, max_length=100, help_text='',
#     #                            widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
#     # email = forms.CharField(label='', required=True, max_length=100, help_text='',
#     #                         widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
#     # password = forms.CharField(label='', required=True, max_length=100, help_text='',
#     #                            widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
