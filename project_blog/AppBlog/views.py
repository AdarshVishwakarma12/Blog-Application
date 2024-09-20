from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(
        request,
        "AppBlog/home.html",
        context
    )

def blog_about(request):
    return HttpResponse("<p> About Page </p>")