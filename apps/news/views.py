from django.shortcuts import render

from apps.news.models import News, NewsCategory
from django.conf import settings

from apps.news.serializers import NewsSerializer
from utils import restful


def index(request):
    """首页"""
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.order_by("-pub_time")[0: count]
    categories = NewsCategory.objects.all()
    context = {
        "newses": newses,
        "categories": categories
    }
    return render(request, 'news/index.html', context=context)


def news_list(request):
    """新闻列表"""
    page = int(request.GET.get("p", 1))
    category_id = int(request.GET.get("category_id", 0))
    start = (page-1) * settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.all()[start: end]
    else:
        newses = News.objects.filter(category__id=category_id)[start: end]
    serializer = NewsSerializer(newses, many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request, news_id):
    """新闻详情页"""
    return render(request, "news/news_detail.html")


def search(request):
    """搜索页"""
    return render(request, "search/search.html")