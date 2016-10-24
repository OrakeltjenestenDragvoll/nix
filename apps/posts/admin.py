from django.contrib import admin
from apps.posts.models import Post
from apps.posts.models import Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)