from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

from .models import apiKeys, ButtonTable


@login_required()
def index(request):
    template = loader.get_template('bujumbura/bujumbura.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))


@login_required()
def hits_pr_day(request):
    template = loader.get_template('bujumbura/hitsaday.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))


@login_required()
def hits_pr_day_stacked(request):
    template = loader.get_template('bujumbura/hitsadaystacked.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))


@login_required()
def weekday(request):
    template = loader.get_template('bujumbura/weekend.html')
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))


@csrf_exempt
def report(request):
    context = {}
    if request.method == 'POST':
        key = request.POST.get('api_key')
        if key:
            sender = apiKeys.objects.get(key=key)
            if sender:
                skrake = request.POST.get('skranke')
                telefon = request.POST.get('telefon')
                random = request.POST.get('random')
                inputlist = []
                if skrake:
                    temp = ButtonTable.objects.create(sender=sender, button='0')
                    inputlist.append(temp)
                if telefon:
                    temp = ButtonTable.objects.create(sender=sender, button='1')
                    inputlist.append(temp)
                if random:
                    temp = ButtonTable.objects.create(sender=sender, button='2')
                    inputlist.append(temp)
                context = {
                    'added': inputlist
                }
    return render(request, 'bujumbura/test.html', context)


def get_key(request):
    qs = apiKeys.objects.all()
    stringset = []
    for item in qs:
        stringset.append(str(item))
    context = {
        'list': stringset
    }
    return render(request, 'bujumbura/test.html', context)
