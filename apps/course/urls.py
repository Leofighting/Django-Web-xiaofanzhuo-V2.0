# -*- coding:utf-8 -*-
__author__ = "leo"

from django.urls import path

from apps.course import views

app_name = "course"

urlpatterns = [
    path("", views.course_index, name="course_index"),
    path("<int:course_id>", views.course_detail, name="course_detail"),
]