from django.conf import settings
from django.core.management.base import BaseCommand
from apps.printers.models import Printer
import urllib2
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        printer_list = Printer.objects.all()
        data = json.load(urllib2.urlopen(settings.PRINTMON_URL + '/index'))
        for printer in printer_list:
            print printer.name
        print data
