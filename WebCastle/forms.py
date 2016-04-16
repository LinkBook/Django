from django import forms


# User = Reg()


# class RegisterForm(forms.ModelForm):
class RegisterForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password', 'repassword']

    username = forms.CharField(label='', required=True, max_length=100, help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.CharField(label='', required=True, max_length=100, help_text='',
                            widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    password = forms.CharField(label='', required=True, max_length=100, help_text='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    repassword = forms.CharField(label='', required=True, max_length=100, help_text='',
                                 widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))
