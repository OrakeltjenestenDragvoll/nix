from django.contrib import admin
from apps.printers.models import Printer, PaperLogEntry
# Register your models here.

admin.site.register(Printer)
admin.site.register(PaperLogEntry)