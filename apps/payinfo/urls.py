# -*- coding:utf-8 -*-
__author__ = "leo"

from django.urls import path
from apps.payinfo import views

app_name = "payinfo"

urlpatterns = [
    path("", views.payinfo, name="payinfo"),
    path("notify_view/", views.notify_view, name="notify_view"),
    path("download/", views.download, name="download"),
    path("payinfo_order/", views.payinfo_order, name="payinfo_order"),
]