from django.urls import path
from . import views

urlpatterns = [
	path("", views.demo, name="demo"),
	path("bg/", views.bg, name="bg"),
	path("<int:pk>/", views.printer, name="printer")
]
