from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.category_description


class Post(models.Model):
    user = models.ForeignKey(User, unique=False)
    content = models.TextField()
    published = models.DateTimeField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.content

