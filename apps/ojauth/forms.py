from django import forms

from apps.forms import FormMixmin
from .models import Users


class LoginForm(forms.Form, FormMixmin):
    user_id = forms.CharField(max_length=48)
    password = forms.CharField(max_length=12, min_length=6, error_messages={"max_length":"密码最多不能超过12位！",
                                                                            "min_length":"密码最少不能少于6位！"})


class RegisterFrom(forms.Form, FormMixmin):
    user_id = forms.CharField(max_length=48)
    nick = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=12, min_length=6, error_messages={"max_length":"密码最多不能超过12位！",
                                                                            "min_length":"密码最少不能少于6位！"})
    password2 = forms.CharField(max_length=12, min_length=6, error_messages={"max_length":"密码最多不能超过12位！",
                                                                            "min_length":"密码最少不能少于6位！"})
    email = forms.EmailField()
    school = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super(RegisterFrom, self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致！')

        user_id = cleaned_data.get('user_id')

        exists = Users.objects.filter(user_id=user_id).exists()
        if exists:
            raise forms.ValidationError('该账号已经被注册！')
