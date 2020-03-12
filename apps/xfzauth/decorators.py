# -*- coding:utf-8 -*-
__author__ = "leo"

from utils import restful
from django.shortcuts import redirect


def xfz_login_required(func):
    """登陆验证"""

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return restful.un_auth(message="请先登录，再做评论~")
            else:
                return redirect("/")

    return wrapper
