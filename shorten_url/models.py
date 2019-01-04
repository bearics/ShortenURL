from django.db import models


# Create your models here.

class Url(models.Model):
    original_url = models.CharField(max_length=50)
    shortened_url = models.CharField(max_length=50)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
