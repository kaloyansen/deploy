from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .otverka import safeStyle
from .context_processors import get_visitor
from work.models import Visitor



def get_lang(request):

	fliplang = request.POST.get("fliplang", False)
	if fliplang: return fliplang[:2]

	visitor = get_visitor(request)
	if not visitor: return 'fr'
	return visitor.lang[:2]


def base(request):
	return render(request, 'base.html', {})


def index(request):
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	title = {'fr': 'développeur back-end',
			 'en': 'backend developer'}
	about = {'fr': 'conception d\'applications, développement back-end, analyse de données scientifique et visualisation en-ligne',
			 'en': 'software designer, backend developer, scientific data analysis and visualisation online'}
			 
	opt = get_lang(request)
	context = {
		'title': title[opt],
		'about': about[opt],
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
		'lange': 'python, C++, java, perl, fortran, c, php, javascript',
		'techno': 'django, pandas, gnuplot, emacs, oracle, mysql, sql*loader, symfony, vue.js, react.js, angular',
		'num_visits': num_visits
	}
	return render(request, 'index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def face(request):
	context = {'style': safeStyle('zero'),
			   'style1': safeStyle('une'),
			   'style2': safeStyle('deux'),
			   'visit': Visitor.objects.all().order_by('date')}
	return render(request, 'face.html', context)


def posoka(request):
	return redirect('/datakosmata')


