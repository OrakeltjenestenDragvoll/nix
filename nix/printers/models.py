from django.db import models
from django.contrib.auth.models import User


class Printer(models.Model):
    name = models.CharField(max_length=10)
    paper = models.TextField()

    def __unicode__(self):
        return self.name


class Log(models.Model):
    printer = models.ForeignKey(Printer, unique=False)
    paper = models.TextField()
    time = models.DateTimeField()
    user = models.ForeignKey(User, unique=False)

    def __unicode__(self):
        return self.paper