from django.urls import path

from .views import blog_home
from .views import blog_about

urlpatterns = [
	path(
		route = "",
		view = blog_home,
		name = "blog-index"
	),

	path(
		route = "blog/",
		view = blog_home,
		name = "blog-home"
	),

	path(
		route = "about",
		view = blog_about,
		name = "blog-about"
	),
]