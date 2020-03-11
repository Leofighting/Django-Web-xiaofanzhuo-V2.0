# -*- coding:utf-8 -*-
__author__ = "leo"

from django.urls import path
from apps.payinfo import views

app_name = "payinfo"

urlpatterns = [
    path("", views.payinfo, name="payinfo"),
]