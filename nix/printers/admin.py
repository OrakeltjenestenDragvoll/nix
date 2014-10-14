from django.contrib import admin
from printers.models import Printer, Log
# Register your models here.

admin.site.register(Printer)
admin.site.register(Log)