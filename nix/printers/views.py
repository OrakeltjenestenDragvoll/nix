from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from printers.models import Printer
import datetime

@login_required(login_url='/admin/')
def index(request):
    printer_list = Printer.objects.order_by('-name')
    template = loader.get_template('printers/index.html')
    context = RequestContext(request, {
        'printer_list': printer_list,
    })
    #return HttpResponse(template.render(context))
    return HttpResponseRedirect('/')

def get_printers(request):

    return HttpResponseRedirect('/')


def update(request):
    if request.method == 'POST':
            current_printers = Printer.objects.all()

            for current_printer in current_printers:
                if float(request.POST[current_printer.name]) > 0:
                    current_printer.paper_text = request.POST[current_printer.name]
                    current_printer.paper_remaining = float(request.POST[current_printer.name]) * 2500
                    current_printer.save()


            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:

        return HttpResponseRedirect('/')