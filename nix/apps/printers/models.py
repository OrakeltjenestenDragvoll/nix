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


class PaperLogEntry(models.Model):
    user = models.ForeignKey(User, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.user) + ':' + unicode(self.date)