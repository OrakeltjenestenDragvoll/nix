from django.db import models
import uuid


class apiKeys(models.Model):
    id = models.CharField(max_length=200, null=False, blank=False)
    key = models.TextField(primary_key=True, default=uuid.uuid4().hex)

    def __unicode__(self):
        return self.id


class ButtonTable(models.Model):
    SKRANKE = 0
    TELEFON = 1
    RANDOM = 2
    BUTTON_CHOICES= (
        (SKRANKE, 'Skranke'),
        (TELEFON, 'Telefon'),
        (RANDOM, 'Random')
    )
    sender = models.ForeignKey(apiKeys, editable=False, null=False)
    button = models.IntegerField(choices=BUTTON_CHOICES, default=0)
    date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.button)

    class Meta:
        verbose_name_plural = 'Case registers'
        verbose_name = 'Registered case'
