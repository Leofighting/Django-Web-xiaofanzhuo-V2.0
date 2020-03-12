import os

import qiniu
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST, require_GET
from django.views.generic.base import View

from apps.cms.forms import EditNewsCategoryForm, WriteNewsForm
from apps.news.models import NewsCategory, News
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
