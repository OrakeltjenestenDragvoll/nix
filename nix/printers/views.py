from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from printers.models import Printer,Log
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
            current_printers = Printer.objects
            current_logs = Log.objects.order_by('-time')[:len(current_printers)]
            updated_statuses = []

            for current_printer in current_printers:
                updated_statuses.add(request.POST[current_printer.name])

            post_content = request.POST['content']
            post_user = request.user
            now = datetime.datetime.now()
            cat = Category.objects.get(category_description='Printer')
            # process the data in form.cleaned_data as required

            post = Post(
                user = post_user,
                content = post_content,
                published = now,
                category = cat,
            )
            post.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return HttpResponseRedirect('/')