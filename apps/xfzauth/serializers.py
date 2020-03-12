# -*- coding:utf-8 -*-
__author__ = "leo"

from rest_framework import serializers

from apps.xfzauth.models import User


class UserSerializer(serializers.ModelSerializer):
    """用户信息序列化"""
    class Meta:
        model = User
        fields = ("uid", "telephone", "username", "email", "is_staff", "is_active")