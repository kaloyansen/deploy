from django.urls import path
from . import views

urlpatterns = [
	path("", views.demo, name="demo"),
	path("bg/", views.bg, name="bg")
	# path("plotter/<int:pk>/", views.plotter, name="plotter"),
	# path("<int:pk>/", views.plotter, name="plotter")
]
