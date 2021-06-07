from django.db import models

class News(models.Model):
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    text = models.TextField(max_length=10000)