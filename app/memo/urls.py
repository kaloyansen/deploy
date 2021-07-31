from django.urls import path
from . import views

urlpatterns = [
	path("demo/", views.demo, name = "demo"),
	path("bg/", views.bg, name = "bg"),
	path("sun/", views.sun, name = "sun")
	# path("plotter/<int:pk>/", views.plotter, name="plotter"),
	# path("<int:pk>/", views.plotter, name="plotter")
]
