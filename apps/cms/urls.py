# -*- coding:utf-8 -*-
__author__ = "leo"

from django.urls import path

from apps.cms import views

app_name = "cms"

urlpatterns = [
    path("cms_index/", views.cms_index, name="cms_index"),
    path("news_category/", views.news_category, name="news_category"),
    path("add_news_category/", views.add_news_category, name="add_news_category"),
    path("edit_news_category/", views.edit_news_category, name="edit_news_category"),
    path("delete_news_category/", views.delete_news_category, name="delete_news_category"),
    path("upload_file/", views.upload_file, name="upload_file"),
    path("qntoken/", views.qntoken, name="qntoken"),
    path("banner/", views.banner, name="banner"),
    path("write_news/", views.WriteNewsView.as_view(), name="write_news"),
]
