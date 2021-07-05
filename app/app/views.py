from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse
# from .models import Page

def base(request):
	return render(request, 'base.html', {})


def index(request):

	context = {
		'title': 'développeur back-end',
		'image': '/img/kalo.png',
		'im1': '/img/mtv.png',
        'im2': '/img/calice.png',
        'im3': '/img/web.png',
        'about': 'conception et développement d\'applications, analyse de données scientifique et visualisation en-ligne',
        'lange': 'python, C++, java, perl, fortran, c, php, javascript',
        'techno': 'django, pandas, gnuplot, emacs, oracle, mysql, sql*loader, symfony, vue.js, react.js, angular'
    }
	return render(request, 'index.html', context)


def posoka(request):
	return redirect('/datakosmata')
