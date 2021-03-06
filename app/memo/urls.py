from django.urls import re_path
from . import views
from app.views import erreur as errr

urlpatterns = [
	re_path('^[/]?$', views.demo, name = 'demo'),
	re_path('^demo[/]?$', views.demo, name = 'demo'),
	re_path('^bg[/]?$', views.bg, name = 'bg'),
	re_path('^bgbg[bg]*[/]?$', views.bgbg, name = 'bgbg'),
	re_path('^bg/bg[/bg]*[/]?$', views.bgbgbg, name = 'bgbgbg'),
	re_path('^spider[/]?$', views.spider, name = 'spider'),
	re_path('^strategy[/]?$', views.strategy, name = 'strategy'),
	re_path('^sun[/]?$', views.sun, name = 'sun'),
	re_path('.*', errr, name = 'erreur')
]
