# -*- coding:utf-8 -*-
__author__ = "leo"

from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.utils.decorators import method_decorator

from apps.xfzauth.decorators import xfz_superuser_required
from apps.xfzauth.models import User


@xfz_superuser_required
def staff_index(request):
    """员工管理首页"""
    staffs = User.objects.filter(is_staff=True)
    context = {
        "staffs": staffs
    }
    return render(request, "cms/staff.html", context=context)


@method_decorator(xfz_superuser_required, name="dispatch")
class AddStaffView(View):
    """添加员工"""
    def get(self, request):
        groups = Group.objects.all()
        context = {
            "groups": groups
        }
        return render(request, "cms/add_staff.html", context=context)

    def post(self, request):
        telephone = request.POST.get("telephone")
        user = User.objects.filter(telephone=telephone).first()
        if user:
            user.is_staff = True
            group_ids = request.POST.getlist("groups")
            groups = Group.objects.filter(pk__in=group_ids)
            user.groups.set(groups)
            user.save()
            return redirect(reverse("cms:staff_index"))
        else:
            messages.info(request, "该手机号码未注册~")
            return redirect(reverse("cms:add_staff"))
