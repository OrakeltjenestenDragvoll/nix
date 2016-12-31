from django.db import models
from django.contrib.auth.models import User


class Printer(models.Model):
    name = models.CharField(max_length=20)
    paper_remaining = models.IntegerField(blank=True, null=True, default=0)
    last_read = models.IntegerField(blank=True, null=True, default=0)
    low_threshold = models.IntegerField(blank=True, null=True, default=0)
    medium_threshold = models.IntegerField(blank=True, null=True, default=0)
    status = models.CharField(blank=True, null=True, max_length=50)

    def __unicode__(self):
        return self.name


class PaperLogEntry(models.Model):
    user = models.ForeignKey(User, unique=False)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.user) + ':' + unicode(self.date)

    class Meta:
        ordering = ['-date']
