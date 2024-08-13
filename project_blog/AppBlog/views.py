from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse(
        "<h1> Welcome to home page </h1>"
    )