# -*- coding:utf-8 -*-
__author__ = "leo"

from django.shortcuts import render


def pub_course(request):
    """发布课程"""
    return render(request, "cms/pub_course.html")
