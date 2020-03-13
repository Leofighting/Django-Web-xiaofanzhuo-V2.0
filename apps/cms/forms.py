# -*- coding:utf-8 -*-
__author__ = "leo"

from django import forms

from apps.forms import FormMixin
from apps.news.models import News, Banner


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


class AddBannerForm(forms.ModelForm, FormMixin):
    """添加轮播图表单"""

    class Meta:
        model = Banner
        fields = ("priority", "link_to", "image_url")


class EditBannerForm(forms.ModelForm, FormMixin):
    """编辑轮播图表单"""
    pk = forms.IntegerField()

    class Meta:
        model = Banner
        fields = ("priority", "link_to", "image_url")


class EditNewsForm(forms.ModelForm, FormMixin):
    """修改新闻表单"""
    category = forms.IntegerField()
    pk = forms.IntegerField()

    class Meta:
        model = News
        exclude = ("category", "author", "pub_time")