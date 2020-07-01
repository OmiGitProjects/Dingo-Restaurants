from django.shortcuts import render
from .models import BlogsDatabase
from django.contrib.auth.decorators import login_required

def blogPage(request):

        blogs = BlogsDatabase.objects.all()[::-1]

        context = {'blogs':blogs}

        return render(request, 'blogs/blog.html', context)