from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post, Category
from django.template import RequestContext, loader
from printers.models import Printer
from posts.forms import PostForm
import datetime


@login_required(login_url='/admin/')
def index(request):
    latest_post_list = Post.objects.order_by('-published')[:5]
    printer_list = Printer.objects.order_by('-name')
    template = loader.get_template('posts/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
        'printer_list': printer_list,
    })
    return HttpResponse(template.render(context))


def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

def post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post_content = request.POST['content']
            post_user = request.user
            now = datetime.datetime.now()
            cat = Category.objects.get(category_description='Info')
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