from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from apps.printers.models import Printer, PaperLogEntry
from apps.posts.models import Post, Category
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


@login_required(login_url='/admin/')
def update(request):
    if request.method == 'POST':
            current_printers = Printer.objects.all()
            for current_printer in current_printers:
                if float(request.POST[current_printer.name]) > 0:
                    current_printer.paper_text = request.POST[current_printer.name]
                    current_printer.paper_remaining = float(current_printer.paper_text) * 2500
                    current_printer.save()
            now = datetime.datetime.now()
            log_user = request.user
            log_entry = PaperLogEntry()
            log_entry[log_user] = log_user
            log_entry.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('/')


def printmon(request):
    printer_list = Printer.objects.order_by('-name')
    template = loader.get_template('printers/printmon.html')
    context = RequestContext(request, {
        'printer_list': printer_list,
    })
    return HttpResponse(template.render(context))


def printskjerm(request):
    printer_list = Printer.objects.order_by('-name')
    cat = Category.objects.filter(category_description='Infoskjerm')
    message_list = Post.objects.order_by('published').filter(category=cat).reverse()[:2]
    template = loader.get_template('printers/printskjerm.html')
    context = RequestContext(request, {
        'printer_list': printer_list,
        'message_list': message_list
    })
    return HttpResponse(template.render(context))