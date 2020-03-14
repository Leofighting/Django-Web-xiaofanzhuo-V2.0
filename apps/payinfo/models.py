from django.db import models


class PayInfo(models.Model):
    """付费咨询"""
    title = models.CharField(max_length=100)
    profile = models.CharField(max_length=200)
    price = models.FloatField()
    path = models.FilePathField()


