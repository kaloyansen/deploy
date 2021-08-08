from django.shortcuts import render, redirect
from django.http import HttpResponse


def base(request):
	return render(request, 'base.html', {})


def index(request):
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	context = {
		'title': 'développeur back-end',
		'title_en': 'backend developer',
		'image': '/img/kalo.png',
		'slide': '/img/slideshow.gif',
		'apirest': '/img/800x600/api.rest.png',
		'basicdjango': '/img/800x600/basic-django.png',
		'django': '/img/800x600/django.png',
		'djangorest': '/img/800x600/django.rest.png',
		'framework': '/img/800x600/framework.png',
		'langage': '/img/800x600/langage.png',
		'mtv': '/img/800x600/mtv.png',
		'mvc': '/img/800x600/mvc.png',
		'mvcr': '/img/800x600/mvcr.png',
		'restendpoint': '/img/800x600/rest.endpoint.png',
		'rsa': '/img/800x600/rsa.png',
		'serverless': '/img/800x600/serverless.png',
		'web': '/img/800x600/web.png',
		'about': 'conception d\'applications, développement back-end, analyse de données scientifique et visualisation en-ligne',
		'about_en': 'software designer, backend developer, scientific data analysis and visualisation online',
		'lange': 'python, C++, java, perl, fortran, c, php, javascript',
		'techno': 'django, pandas, gnuplot, emacs, oracle, mysql, sql*loader, symfony, vue.js, react.js, angular, react',
		'num_visits': num_visits
	}
	return render(request, 'index.html', context)


def posoka(request):
	return redirect('/datakosmata')
