# -*- coding:utf-8 -*-
__author__ = "leo"

from django import forms

from apps.forms import FormMixin


class PublicComment(forms.Form, FormMixin):
    """新闻评论表单"""
    content = forms.CharField()
    news_id = forms.IntegerField()
