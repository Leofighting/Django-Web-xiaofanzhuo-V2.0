import time
import os
import hmac
import hashlib
from hashlib import md5

from django.conf import settings
from django.http import Http404
from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt

from apps.course.models import Course, CourseOrder
from apps.xfzauth.decorators import xfz_login_required
from utils import restful


def course_index(request):
    """课程首页"""
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "course/course_index.html", context=context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)

    except Course.DoesNotExist:
        raise Http404

    buyed = CourseOrder.objects.filter(course=course, buyer=request.user, status=2).exists()
    context = {
        "course": course,
        "buyed": buyed
    }
    return render(request, "course/course_detail.html", context=context)


def course_token(request):
    file = request.GET.get('video')

    course_id = request.GET.get('course_id')
    if not CourseOrder.objects.filter(course_id=course_id, buyer=request.user, status=2).exists():
        return restful.params_error(message='请先购买课程！')

    expiration_time = int(time.time()) + 2 * 60 * 60

    USER_ID = settings.BAIDU_CLOUD_USER_ID
    USER_KEY = settings.BAIDU_CLOUD_USER_KEY

    extension = os.path.splitext(file)[1]
    media_id = file.split('/')[-1].replace(extension, '')

    key = USER_KEY.encode('utf-8')
    message = '/{0}/{1}'.format(media_id, expiration_time).encode('utf-8')
    signature = hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, USER_ID, expiration_time)
    return restful.result(data={'token': token})


@xfz_login_required
def course_order(request, course_id):
    """课程订单"""
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404

    order = CourseOrder.objects.create(course=course, buyer=request.user)
    context = {
        "course": course,
        "order": order,
        "notify_url": request.build_absolute_uri(reverse("course:notify_view")),
        "return_url": request.build_absolute_uri(
            reverse("course:course_detail", kwargs={"course_id": course.pk}))
    }

    return render(request, "course/course_order.html", context=context)


@xfz_login_required
def course_order_key(request):
    goodsname = request.POST.get("goodsname")
    istype = request.POST.get("istype")
    notify_url = request.POST.get("notify_url")
    orderid = request.POST.get("orderid")
    price = request.POST.get("price")
    return_url = request.POST.get("return_url")
    token = 'e6110f92abcb11040ba153967847b7a6'
    uid = '49dc532695baa99e16e01bc0'
    orderuid = str(request.user.pk)
    key = md5((goodsname + istype + notify_url + orderid + orderuid + price + return_url + token + uid).encode(
        "utf-8")).hexdigest()
    return restful.result(data={"key": key})


@csrf_exempt
def notify_view(request):
    order_id = request.POST.get("orderid")
    Course.objects.filter(pk=order_id).update(status=2)
    return restful.ok()
