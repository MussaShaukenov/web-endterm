from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)