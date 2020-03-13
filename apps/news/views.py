from django.http import Http404
from django.shortcuts import render

from apps.news.forms import PublicComment
from apps.news.models import News, NewsCategory, Comment, Banner
from django.conf import settings

from apps.news.serializers import NewsSerializer, CommentSerializer
from apps.xfzauth.decorators import xfz_login_required
from utils import restful


def index(request):
    """首页"""
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.select_related("category", "author").all()[0: count]
    categories = NewsCategory.objects.all()
    context = {
        "newses": newses,
        "categories": categories,
        "banners": Banner.objects.all()
    }
    return render(request, 'news/index.html', context=context)


def news_list(request):
    """新闻列表"""
    page = int(request.GET.get("p", 1))
    category_id = int(request.GET.get("category_id", 0))
    start = (page - 1) * settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.select_related("category", "author").all()[start: end]
    else:
        newses = News.objects.filter(category__id=category_id)[start: end]
    serializer = NewsSerializer(newses, many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request, news_id):
    """新闻详情页"""
    try:
        news = News.objects.select_related("author", "category").prefetch_related("comments__author").get(pk=news_id)
        context = {
            "news": news
        }
        return render(request, "news/news_detail.html", context=context)
    except News.DoesNotExist:
        raise Http404


def search(request):
    """搜索页"""
    return render(request, "search/search.html")


@xfz_login_required
def public_comment(request):
    """新闻评论"""
    form = PublicComment(request.POST)
    if form.is_valid():
        news_id = form.cleaned_data.get("news_id")
        content = form.cleaned_data.get("content")
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(news=news, content=content, author=request.user)
        serializer = CommentSerializer(comment)

        return restful.result(data=serializer.data)
    else:
        return restful.params_error(message=form.get_errors())
