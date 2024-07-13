from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publishingCountry = models.CharField(max_length=200, blank=True)
    publishDate = models.DateTimeField(auto_now=True)
