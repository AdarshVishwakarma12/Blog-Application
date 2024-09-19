from django.shortcuts import render
from django.http import HttpResponse

def blog_home(request):
    return render(
        request,
        "AppBlog/home.html"
    )

def blog_about(request):
    return HttpResponse("<p> About Page </p>")