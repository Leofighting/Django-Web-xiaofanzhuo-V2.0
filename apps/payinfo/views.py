from django.shortcuts import render

from apps.payinfo.models import PayInfo


def payinfo(request):
    """付费咨询"""
    context = {
        "payinfos": PayInfo.objects.all()
    }
    return render(request, "payinfo/payinfo.html", context=context)

