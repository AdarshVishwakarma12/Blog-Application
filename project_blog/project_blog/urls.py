from django.contrib import admin
from django.urls import path

# Importing App views
from AppBlog import views as AppBlog_views

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    path(
        "blog/",
        AppBlog_views.blog_home,
        name="blog-home"
    ),
    path(
        "",
        AppBlog_views.blog_home,
    )
]