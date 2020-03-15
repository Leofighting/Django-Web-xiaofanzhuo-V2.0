# -*- coding:utf-8 -*-
__author__ = "leo"

from haystack import indexes

from apps.news.models import News


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    """新闻索引"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
