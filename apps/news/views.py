from django.shortcuts import render

from apps.news.models import News, NewsCategory


def index(request):
    """首页"""
    newses = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {
        "newses": newses,
        "categories": categories
    }
    return render(request, 'news/index.html', context=context)


def news_detail(request, news_id):
    """新闻详情页"""
    return render(request, "news/news_detail.html")


def search(request):
    """搜索页"""
    return render(request, "search/search.html")