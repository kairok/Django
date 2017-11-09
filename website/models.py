from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

class area(models.Model):
    name = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name