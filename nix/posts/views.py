from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post, Category
from django.template import RequestContext, loader
from printers.models import Printer
from posts.forms import PostForm
import datetime
from django.core.mail import EmailMessage

@login_required(login_url='/admin/')
def index(request):
    latest_post_list = Post.objects.order_by('-published')[:5]
    printer_list = Printer.objects.order_by('-name')
    categories = Category.objects.all()
    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'printer_list': printer_list,
        'categories': categories,

    })
    return HttpResponse(template.render(context))


def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

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
    email = EmailMessage('Hello', 'World', to=['user@gmail.com'])
    email.send()
    return HttpResponseRedirect('/')