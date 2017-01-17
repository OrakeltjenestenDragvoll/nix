import json

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from nix import settings
import datetime

from .models import apiKeys, ButtonTable

@login_required()
def hits_pr_day(request):
    context = {
    }
    return render(request, 'bujumbura/hitsaday.html', context)


@login_required()
def hits_pr_day_stacked(request):
    context = {
    }
    return render(request, 'bujumbura/hitsadaystacked.html', context)


@login_required()
def weekday(request):
    context = {
    }
    return render(request, 'bujumbura/weekday.html', context)


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


@login_required()
def get_last_monthly(request):
    data = {
    }
    for d in (timezone.now().date() - timezone.timedelta(days=x) for x in
              range(0, 30)):
        data.update({str(d):
                         {'a': 0, 'b': 0, 'c': 0}
                     })
    if settings.DEBUG is False:
        a_query = get_button_count(0, 30)
        for element in a_query:
            data.get(element['date'].isoformat()).update(a=element['button_count'])
        b_query = get_button_count(1, 30)
        for element in b_query:
            data.get(element['date'].isoformat()).update(b=element['button_count'])
        c_query = get_button_count(2, 30)
        for element in c_query:
            data.get(element['date'].isoformat()).update(c=element['button_count'])
    else:
        a_query = get_button_count(0, 30)
        for element in a_query:
            data.get(element['date']).update(a=element['button_count'])
        b_query = get_button_count(1, 30)
        for element in b_query:
            data.get(element['date']).update(b=element['button_count'])
        c_query = get_button_count(2, 30)
        for element in c_query:
            data.get(element['date']).update(c=element['button_count'])

    return HttpResponse(json.dumps(data, sort_keys=True), content_type='application/json')


@login_required()
def get_weekday(request):
    name = ['Lordag', 'Sondag', 'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']
    data = {}
    for d in range(0, 7):
        data.update({str(d):
                         {'day': name[d], 'tot': 0, 'a': 0, 'b': 0, 'c': 0}
                     })
    for x in range(0, 8):
        total = 0
        temp_weekday = get_weekday_count(x)
        for element in temp_weekday:
            if element['button'] == 0:
                data.get(str(x)).update(a=element['count'])
            elif element['button'] == 1:
                data.get(str(x)).update(b=element['count'])
            elif element['button'] == 2:
                data.get(str(x)).update(c=element['count'])
            total += element['count']
        if total != 0:
            data.get(str(x)).update(tot=total)

    return HttpResponse(json.dumps(data, sort_keys=True), content_type='application/json')


def get_button_count(button_id, days_back):
    return ButtonTable.objects.filter(button=button_id, date_registered__date__lte=timezone.now(),
                                      date_registered__date__gt=timezone.now() - timezone.timedelta(
                                          days=days_back)).extra({'date': "date(date_registered)"}).values(
        'date').annotate(button_count=Count('id'))


def get_weekday_count(weekday):
    return ButtonTable.objects.filter(date_registered__week_day=weekday).values('button').annotate(
        count=Count('button'))
