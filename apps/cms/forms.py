# -*- coding:utf-8 -*-
__author__ = "leo"

from django import forms

from apps.forms import FormMixin
from apps.news.models import News


class EditNewsCategoryForm(forms.Form, FormMixin):
    """修改新闻分类"""
    pk = forms.IntegerField(error_messages={
        "required": "必须传入新闻分类的id~"
    })
    name = forms.CharField(max_length=100)


class WriteNewsForm(forms.ModelForm, FormMixin):
    """编辑新闻表单"""
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ["category", "author", "pub_time"]
