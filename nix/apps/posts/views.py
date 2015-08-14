# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from apps.posts.models import Post, Category
from django.template import RequestContext, loader
from apps.printers.models import Printer
from apps.posts.forms import PostForm
import datetime
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404



@login_required(login_url='/admin/')
def index(request):
    latest_post_list = Post.objects.order_by('-published')[:10]
    printer_list = Printer.objects.order_by('-name')
    categories = Category.objects.all()
    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'printer_list': printer_list,
        'categories': categories,

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
            now = datetime.datetime.now()

            post = Post(
                user = post_user,
                content = post_content,
                published = now,
                category = post_category,
            )
            post.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

@login_required(login_url='/admin/')
def order(request):
    subject = "Papirbestilling Orakel Dragvoll"
    content = "Hei!\n\nTrenger å bestille en/to pall(er) (48/96 kasser) A4-papir.\n\n" \
              "Mottaker er Orakeltjenesten Dragvoll, bygg 8, nivå 5 Leveringssted er ved heis 7, nivå 2 (mellom bygg 6 og 8), NTNU Dragvoll, Edvard Bulls veg 1\n\n" \
              "Kontaktinfo som transportøren kan ringe: Orakeltjenesten Dragvoll, tlf. 735 91810, \n\n" \
              "Prosjektnummer.: 09115000 K-sted: 167325"\
              "Denne eposte-adressen brukes ikke. Kontakt dragvollorakel@ntnu.no ved spørsmål"
    headers = {'Reply-To': "dragvollorakel@ntnu.no"}
    email = EmailMessage(subject, content, to=['utstyrsbestilling@itea.ntnu.no'], headers=headers)
    email.send()
    now = datetime.datetime.now()
    category = Category.objects.get(category_description='Info')
    post = Post(
        user = request.user,
        content = "Papirpalle til nivå 2 er bestilt",
        published = now,
        category = category,
    )
    post.save()
    return HttpResponseRedirect('/')

@login_required(login_url='/admin/')
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id).delete()
    return HttpResponseRedirect('/')