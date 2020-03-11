from django.shortcuts import render


def payinfo(request):
    """付费咨询"""
    return render(request, "payinfo/payinfo.html")
