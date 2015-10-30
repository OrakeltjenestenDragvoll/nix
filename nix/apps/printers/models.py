from django.db import models
from django.contrib.auth.models import User


class Printer(models.Model):
    name = models.CharField(max_length=10)
    paper_text = models.TextField()
    paper_remaining = models.BigIntegerField()
    last_read = models.BigIntegerField()
    low_threshold = models.BigIntegerField()
    medium_threshold = models.BigIntegerField()
    full_threshold = models.BigIntegerField()
    status = models.TextField()

    def __unicode__(self):
        return self.name


class LogEntry(models.Model):
    user = models.ForeignKey(User, unique=False)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.user + self.date
