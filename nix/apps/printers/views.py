from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.printers.models import Printer, PaperLogEntry
from apps.posts.models import Post, Category


@login_required()
def index(request):
    return HttpResponseRedirect('/')


def get_printers(request):
    return HttpResponseRedirect('/')


@login_required()
def update(request):
    if request.method == 'POST':
            current_printers = Printer.objects.all()
            for current_printer in current_printers:
                if float(request.POST[current_printer.name].replace(',', '.')) > 0:
                    current_printer.paper_text = request.POST[current_printer.name].replace(',', '.')
                    current_printer.paper_remaining = float(current_printer.paper_text.replace(',', '.')) * 2500
                    current_printer.save()
            log_user = request.user
            log_entry = PaperLogEntry()
            log_entry.user = log_user
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


def logs(request):
    logs = PaperLogEntry.objects.all()

    paginator = Paginator(logs, 10)
    page = request.GET.get('page')

    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        logs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        logs = paginator.page(paginator.num_pages)


    template = loader.get_template('printers/logs.html')
    context = RequestContext(request, {
        'logs': logs,
    })
    return HttpResponse(template.render(context))