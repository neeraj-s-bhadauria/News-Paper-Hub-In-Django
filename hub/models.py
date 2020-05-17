from django.db import models
from django.contrib.auth.models import User


class NewsSites(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Posts'
