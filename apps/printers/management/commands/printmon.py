from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from apps.printers.models import Printer, PaperLogEntry
import urllib2
import json
from datetime import timedelta

sheets_per_box = 2500.00


class Command(BaseCommand):
    def handle(self, *args, **options):
        printer_list = list(Printer.objects.all())
        data = json.load(urllib2.urlopen(settings.PRINTMON_URL))
        data = byteify(data)
        statuses = {}
        papercount = {}

        for printer in data:
            statuses[printer['name']] = printer['status']
            papercount[printer['name']] = printer['paperCounter']

        for key, value in statuses.iteritems():
            for printer in printer_list:
                if key == printer.name:
                    update_printer(key, value, papercount[key])

        time_threshold = timezone.now()-timedelta(days=1)
        if not PaperLogEntry.objects.filter(date__gte=time_threshold).exists():
            log = PaperLogEntry()
            log.user = User.objects.get(username='printmon')
            log.save()


def update_printer(name, status, lastread):
            printer = Printer.objects.get(name=name)
            difference = lastread - printer.last_read
            printer.paper_remaining = printer.paper_remaining - difference
            printer.status = status
            printer.last_read = lastread
            printer.save()

            if printer.name == '10.3v':
                aux_printer = Printer.objects.get(name='10.3h')
                aux_printer.paper_remaining = printer.paper_remaining - difference
                aux_printer.save()

            if printer.name == '10.3h':
                aux_printer = Printer.objects.get(name='10.3v')
                aux_printer.paper_remaining = aux_printer.paper_remaining - difference
                aux_printer.save()


def byteify(data):
    if isinstance(data, dict):
        return {byteify(key): byteify(value) for key, value in data.iteritems()}
    elif isinstance(data, list):
        return [byteify(element) for element in data]
    elif isinstance(data, unicode):
        return data.encode('utf-8')
    else:
        return data
