from django.conf import settings
from django.core.management.base import BaseCommand
from apps.printers.models import Printer
import urllib2
import json

sheets_per_box = 2500.00

class Command(BaseCommand):
    def handle(self, *args, **options):
        printer_list = list(Printer.objects.all())
        data = json.load(urllib2.urlopen(settings.PRINTMON_URL + '/index'))
        data = byteify(data)
        statuses = {}
        papercount = {}

        for i in range(0, len(printer_list)):
            for y in range(0, len(data)):
                if data[y]['name'] == printer_list[i].name:
                    statuses[data[i]['name']] = data[i]['status']
                    papercount[data[i]['name']] = data[i]['paperCounter']

        print 'JSON length: ' + str(len(data))
        print 'DB length: ' + str(len(printer_list))
        for key in statuses:
            print key + ' : ' + statuses[key]
            print key + ' : ' + str(papercount[key])

        for key, value in statuses.iteritems():
            printer = Printer.objects.get(name=key)
            difference = papercount[key] - printer.last_read
            printer.paper_remaining = printer.paper_remaining - difference
            printer.paper_text = unicode(round(printer.paper_remaining/sheets_per_box, 2))
            printer.status = value
            printer.last_read = papercount[key]
            printer.save()

def update_printer(name, status, lastread):
            printer = Printer.objects.get(name=name)
            difference = lastread - printer.last_read
            printer.paper_remaining = printer.paper_remaining - difference
            printer.paper_text = unicode(round(printer.paper_remaining/sheets_per_box, 2))
            printer.status = status
            printer.last_read = lastread
            printer.save()


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input