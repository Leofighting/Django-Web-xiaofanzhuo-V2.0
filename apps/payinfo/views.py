import os

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt

from apps.payinfo.models import PayInfo, PayInfoOrder
from apps.xfzauth.decorators import xfz_login_required
from utils import restful


def payinfo(request):
    """付费咨询"""
    context = {
        "payinfos": PayInfo.objects.all()
    }
    return render(request, "payinfo/payinfo.html", context=context)


@xfz_login_required
def payinfo_order(request):
    """付费咨询订单"""
    payinfo_id = request.GET.get("payinfo_id")
    payinfo = PayInfo.objects.get(pk=payinfo_id)
    order = PayInfoOrder.objects.create(payinfo=payinfo, buyer=request.user, status=1, amount=payinfo.price)
    context = {
        "goods": {
            "thumbnail": "",
            "price": payinfo.price,
            "title": payinfo.title
        },
        "order": order,
        "notify": request.build_absolute_uri(reverse("payinfo:notify_view")),
        "return_url": request.build_absolute_uri(reverse("payinfo:payinfo"))
    }
    return render(request, "course/course_order.html", context=context)


@csrf_exempt
def notify_view(request):
    orderid = request.POST.get("orderid")
    PayInfoOrder.objects.filter(pk=orderid).update(status=2)
    return restful.ok()


def download(request):
    """下载文件"""
    payinfo_id = request.GET.get("payinfo_id")
    order = PayInfoOrder.objects.filter(payinfo_id=payinfo_id, buyer=request.user, status=2).first()
    if order:
        payinfo = order.payinfo
        path = payinfo.path
        fp = open(os.path.join(settings.MEDIA_ROOT, path), "rb")
        response = FileResponse(fp)
        response["Content-Type"] = "image/jepg"
        response["Content-Disposition"] = "attachment;filename='%s'" % path.split("/")[-1]
        return response
    else:
        return Http404()
