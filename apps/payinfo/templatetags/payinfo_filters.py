# -*- coding:utf-8 -*-
__author__ = "leo"

from django import template

from apps.payinfo.models import PayInfoOrder

register = template.Library()


@register.filter
def is_buyed(payinfo, user):
    if user.is_authenticated:
        result = PayInfoOrder.objects.filter(payinfo=payinfo, buyer=user, status=2).exists()
        return result
    else:
        return True
