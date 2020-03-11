# -*- coding:utf-8 -*-
__author__ = "leo"

from django import forms
from django.core.cache import cache

from apps.forms import FormMixin
from apps.xfzauth.models import User


class LoginForm(forms.Form, FormMixin):
    """登陆表单"""
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=32, min_length=6, error_messages={
        "max_length": "密码最多不能超过32个字符~",
        "min_length": "密码最少不上少于6个字符~"
    })
    remember = forms.IntegerField(required=False)


class RegisterForm(forms.Form, FormMixin):
    """注册验证表单"""
    telephone = forms.CharField(max_length=11)
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=32, min_length=6, error_messages={
        "max_length": "密码最多不能超过32个字符~",
        "min_length": "密码最少不上少于6个字符~"
    })
    password2 = forms.CharField(max_length=32, min_length=6, error_messages={
        "max_length": "密码最多不能超过32个字符~",
        "min_length": "密码最少不上少于6个字符~"
    })
    img_captcha = forms.CharField(min_length=4, max_length=4)
    sms_captcha = forms.CharField(min_length=4, max_length=4)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致~")

        img_captcha = cleaned_data.get("img_captcha").lower()
        cache_img_captcha = cache.get(img_captcha).lower()

        if not cache_img_captcha or cache_img_captcha != img_captcha:
            raise forms.ValidationError("图形验证码错误~")

        telephone = cleaned_data.get("telephone")

        if User.objects.filter(telephone=telephone).exists():
            raise forms.ValidationError("该手机号码已被注册~")

        sms_captcha = cleaned_data.get("sms_captcha")
        cache_sms_captcha = cache.get(telephone)

        if not cache_sms_captcha or cache_sms_captcha != sms_captcha:
            raise forms.ValidationError("短信验证码错误~")
