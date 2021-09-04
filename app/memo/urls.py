from django.urls import path
from . import views

urlpatterns = [
	path("demo/", views.demo, name = "demo"),
	path("bg/", views.bg, name = "bg"),
	path("bg/bg/bg/", views.bgbgbg, name = "bgbgbg"),
	path("spider/", views.spider, name = "spider"),
	path("sun/", views.sun, name = "sun")
]
