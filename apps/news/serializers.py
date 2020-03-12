# -*- coding:utf-8 -*-
__author__ = "leo"

from rest_framework import serializers

from apps.news.models import NewsCategory, News
from apps.xfzauth.serializers import UserSerializer


class NewsCategorySerializer(serializers.ModelSerializer):
    """新闻列表序列化"""
    class Meta:
        model = NewsCategory
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    """新闻序列化"""
    category = NewsCategorySerializer()
    author = UserSerializer()

    class Meta:
        model = News
        fields = ("id", "title", "desc", "thumbnail", "category", "author", "pub_time")
