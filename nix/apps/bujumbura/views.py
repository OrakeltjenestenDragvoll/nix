from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader


#@login_required(login_url='/admin/')
def index(request):
    template = loader.get_template('bujumbura/bujumbura.html')
    context = RequestContext(request, {    })

    return HttpResponse(template.render(context))


#@login_required(login_url='/admin/')
def hits_pr_day(request):
    template = loader.get_template('bujumbura/hitsaday.html')
    context = RequestContext(request, {    })

    return HttpResponse(template.render(context))


#@login_required(login_url='/admin/')
def hits_pr_day_stacked(request):
    template = loader.get_template('bujumbura/hitsadaystacked.html')
    context = RequestContext(request, {    })

    return HttpResponse(template.render(context))


#@login_required(login_url='/admin/')
def weekday(request):
    template = loader.get_template('bujumbura/weekend.html')
    context = RequestContext(request, {    })

    return HttpResponse(template.render(context))
