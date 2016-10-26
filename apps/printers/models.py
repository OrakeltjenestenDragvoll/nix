from django.db import models
from django.contrib.auth.models import User


class Printer(models.Model):
    name = models.CharField(max_length=20)
    paper_remaining = models.IntegerField(blank=True)
    last_read = models.IntegerField(blank=True)
    low_threshold = models.IntegerField(blank=True)
    medium_threshold = models.IntegerField(blank=True)
    full_threshold = models.IntegerField(blank=True)
    status = models.CharField(blank=True, max_length=50)

    def __unicode__(self):
        return self.name


class PaperLogEntry(models.Model):
    user = models.ForeignKey(User, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.user) + ':' + unicode(self.date)

    class Meta:
        ordering = ['-date']
