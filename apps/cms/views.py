import os

import qiniu
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST, require_GET
from django.views.generic.base import View

from apps.cms.forms import EditNewsCategoryForm, WriteNewsForm, AddBannerForm, EditBannerForm
from apps.news.models import NewsCategory, News, Banner
from apps.news.serializers import BannerSerializer
from utils import restful
from xfz.settings import MEDIA_ROOT, MEDIA_URL, QINIU_ACCESS_KEY, QINIU_SECRET_KEY, QINIU_BUCKET_NAME


@staff_member_required(login_url="index")
def cms_index(request):
    """cms后台管理首页"""
    return render(request, "cms/cms_index.html")


class WriteNewsView(View):
    """编辑新闻"""

    def get(self, request):
        categories = NewsCategory.objects.all()
        context = {
            "categories": categories
        }
        return render(request, "cms/write_news.html", context=context)

    def post(self, request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            desc = form.cleaned_data.get("desc")
            thumbnail = form.cleaned_data.get("thumbnail")
            content = form.cleaned_data.get("content")
            category_id = form.cleaned_data.get("category")
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.create(title=title, desc=desc, thumbnail=thumbnail,
                                content=content, category=category, author=request.user)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


@require_GET
def news_category(request):
    """新闻分类"""
    categories = NewsCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "cms/news_category.html", context=context)


@require_POST
def add_news_category(request):
    """添加新闻分类"""
    name = request.POST.get("name")
    if NewsCategory.objects.filter(name=name).exists():
        return restful.params_error(message="该分类已存在~")
    else:
        NewsCategory.objects.create(name=name)
        return restful.ok()


@require_POST
def edit_news_category(request):
    """修改新闻分类"""
    form = EditNewsCategoryForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get("pk")
        name = form.cleaned_data.get("name")
        try:
            NewsCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message="该新闻分类不存在~")
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def delete_news_category(request):
    """删除新闻分类"""
    pk = request.POST.get("pk")
    try:
        NewsCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.un_auth(message="该分类不存在~")


@require_POST
def upload_file(request):
    """上传新闻缩略图"""
    file = request.FILES.get("file")
    name = file.name
    with open(os.path.join(MEDIA_ROOT, name), "wb") as fp:
        for chunk in file.chunks():
            fp.write(chunk)

    url = request.build_absolute_uri(MEDIA_URL + name)
    return restful.result(data={"url": url})


@require_GET
def qntoken(request):
    """七牛云 token"""
    access_key = QINIU_ACCESS_KEY
    secret_key = QINIU_SECRET_KEY
    bucket = QINIU_BUCKET_NAME
    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket)
    return restful.result(data={"token": token})


def banner(request):
    """轮播图"""
    return render(request, "cms/banners.html")


def add_banner(request):
    """添加轮播图"""
    form = AddBannerForm(request.POST)
    if form.is_valid():
        priority = form.cleaned_data.get("priority")
        image_url = form.cleaned_data.get("image_url")
        link_to = form.cleaned_data.get("link_to")
        banner = Banner.objects.create(priority=priority, image_url=image_url, link_to=link_to)
        return restful.result(data={"banner_id": banner.pk})
    else:
        return restful.params_error(message=form.get_errors())


def banner_list(request):
    """轮播图列表"""
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return restful.result(data=serializer.data)


def delete_banner(request):
    """删除轮播图"""
    banner_id = request.POST.get("banner_id")
    Banner.objects.filter(pk=banner_id).delete()
    return restful.ok()


def edit_banner(request):
    """编辑轮播图"""
    form = EditBannerForm(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get("pk")
        image_url = form.cleaned_data.get("image_url")
        link_to = form.cleaned_data.get("link_to")
        priority = form.cleaned_data.get("priority")
        Banner.objects.filter(pk=pk).update(image_url=image_url, link_to=link_to, priority=priority)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())
