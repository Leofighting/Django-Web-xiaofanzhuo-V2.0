from django.db import models


class NewsCategory(models.Model):
    """新闻分类"""
    name = models.CharField(max_length=100)


class News(models.Model):
    """新闻"""
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    thumbnail = models.URLField()
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("NewsCategory", on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey("xfzauth.User", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-pub_time"]
