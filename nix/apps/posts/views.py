# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext, loader
from django.contrib import messages
from apps.posts.models import Post, Category
from apps.printers.models import Printer, PaperLogEntry
from apps.posts.forms import PostForm
import nix.settings as settings
from datetime import datetime


@login_required(login_url='/admin/')
def index(request):
    latest_post_list = Post.objects.order_by('-published')[:10]
    printer_list = Printer.objects.order_by('-name')
    categories = Category.objects.all()
    log = PaperLogEntry.objects.order_by('-date')[:1]
    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'printer_list': printer_list,
        'categories': categories,
        'last_log': log,
    })
    return HttpResponse(template.render(context))


@login_required(login_url='/admin/')
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_content = form.cleaned_data['content']
            post_category_text = form.cleaned_data['category']
            post_category = Category.objects.get(category_description=post_category_text)
            if not post_category:
                post_category = Category.objects.get(category_description='Info')
            post_user = request.user
            now = datetime.now()

            post = Post(
                user=post_user,
                content=post_content,
                published=now,
                category=post_category,
            )
            post.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')
    messages.warning(request, u"Ugyldig post. Fyll inn tekst eller velg kategori")
    return HttpResponseRedirect('/')


@login_required(login_url='/admin/')
def order(request):
    if request.method == 'POST':
        template = loader.get_template('posts/confirm_order.html')
        context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required(login_url='/admin/')
def confirm_order(request):
    if request.method == 'POST':
        num_of_pallets = int(request.POST.get('numberOfPallets'))
        print(num_of_pallets)
        if num_of_pallets == 1:
            num_of_boxes = 48
        elif num_of_pallets == 2:
            num_of_boxes = 96
        else:
            messages.error(request, u"Du kan ikke bestille mer enn 2 paller")
            return HttpResponseRedirect('/')

        subject = "Papirbestilling Orakel Dragvoll"
        content = "Hei!\n\nTrenger å bestille " + str(num_of_pallets) + " pall (" + str(num_of_boxes) + " kasser) A4-papir.\n\n" \
                  "Mottaker er Orakeltjenesten Dragvoll, bygg 8, nivå 5 Leveringssted er ved heis 7, nivå 2 (mellom bygg 6 og 8), NTNU Dragvoll, Edvard Bulls veg 1\n\n" \
                  "Kontaktinfo som transportøren kan ringe: Orakeltjenesten Dragvoll, tlf. 735 91810, \n\n" \
                  "Prosjektnummer.: 09115000 K-sted: 167325"\
                  "\nDenne eposte-adressen brukes bare til sending av bestilling. Kontakt dragvollorakel@ntnu.no ved spørsmål"
        headers = {'Reply-To': "dragvollorakel@ntnu.no"}
        email = EmailMessage(subject, content, to=[settings.ORDER_TARGET_EMAIL, settings.ORDER_COPY_EMAIL], headers=headers)
        email.send()
        now = datetime.datetime.now()
        category = Category.objects.get(category_description='Info')
        post = Post(
            user=request.user,
            content="",
            published=now,
            category=category,
        )
        if num_of_pallets == 1:
            post.content='En papirpalle er bestilt til nivå 2'
        if num_of_pallets == 2:
            post.content='To papirpaller er bestilt til nivå 2'
        post.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/admin/')
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user.id is request.user.id:
        messages.success(request, u"Posten ble slettet")
        post.delete()
    else:
        messages.error(request, u"Du kan ikke slette denne posten")

    return HttpResponseRedirect('/')