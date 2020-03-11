from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.http import require_POST
from django.core.cache import cache
from django.contrib.auth import get_user_model

from apps.xfzauth.forms import LoginForm, RegisterForm
from utils import restful
from utils.aliyunsdk import aliyunsms
from utils.captcha.xfzcaptcha import Captcha

User = get_user_model()


@require_POST
def login_views(request):
    """登陆"""
    form = LoginForm(request.POST)

    if form.is_valid():
        telephone = form.cleaned_data.get("telephone")
        password = form.cleaned_data.get("password")
        remember = form.cleaned_data.get("remember")
        user = authenticate(request, username=telephone, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.un_auth(message="该账号已被冻结~")
        else:
            return restful.params_error(message="手机号码或者密码错误~")

    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)


def logout_view(request):
    """退出登录"""
    logout(request)
    return redirect(reverse("index"))


def img_captcha(request):
    """验证码图片"""
    text, image = Captcha.gene_code()
    out = BytesIO()
    image.save(out, "png")
    out.seek(0)
    response = HttpResponse(content_type="image/png")
    response.write(out.read())
    response["Content-length"] = out.tell()
    cache.set(text.lower(), text.lower(), 10*60)
    return response


def sms_captcha(request):
    """短信验证码"""
    telephone = request.GET.get("telephone")
    code = Captcha.gene_number()
    cache.set(telephone, code, 10*60)
    # result = aliyunsms.send_sms(telephone, code)

    print("短信验证码：", code)
    return restful.ok()


@require_POST
def register(request):
    """用户注册"""
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get("telephone")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        print(telephone, username, password)
        user = User.objects.create_user(telephone=telephone, username=username, password=password)
        login(request, user)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())
