from django.db import models
from django.contrib import admin
from apps.utils import TimeStampedModel


class Board(TimeStampedModel):
    title = models.CharField(max_length=64)
    description = models.TextField()


admin.site.register(Board)
