# -*- coding:utf-8 -*-
__author__ = "leo"

from functools import wraps

from django.http import Http404

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


def xfz_superuser_required(view_func):
    @wraps(view_func)
    def decorator(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            raise Http404()

    return decorator

