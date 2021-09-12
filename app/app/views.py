import socket
import logging
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.template import RequestContext
from .otverka import safeStyle
from .context_processors import get_visitor
from work.models import Visitor
from memo.plot import animalien

logger = logging.getLogger(__name__)


def handler400(request, *args, **argv): return handlerxxx(400, 'bad request', request, *args, **argv)

def handler403(request, *args, **argv): return handlerxxx(403, 'permission denied', request, *args, **argv)

def handler404(request, *args, **argv): return handlerxxx(404, 'page not found', request, *args, **argv)

def handler500(request, *args, **argv): return handlerxxx(500, 'error', request, *args, **argv)

def handlerxxx(code, message, request, *args, **argv):
	message = '[{}] {}<br />** {} **'.format(code, message, request.path_info)
	response = render(request, 'erreur.html', {'message': "<strong><p>{}</p></strong>if you like it is possible to send an e-mail to".format(message)})
	response.status_code = code
	return response


def get_lang(request):

	fliplang = request.POST.get("fliplang", False)
	if fliplang: return fliplang[:2]

	visitor = get_visitor(request)
	if not visitor: return 'fr'
	return visitor.lang[:2]


def base(request): return render(request, 'base.html')
def erreur(request): return render(request, 'erreur.html', {'message': "<p>something wrong or at least not forseen happened</p>if you like it is possible to send an e-mail to"})



def index(request):
	logger.info('index')
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	title = {'fr': 'développeur back-end',
			 'en': 'backend developer'}
	about = {'fr': '<p>conception d\'applications</p><p>développement back-end</p><p>analyse de données scientifique</p><p>visualisation en-ligne</p>',
			 'en': '<p>software design</p><p>backend development</p><p>scientific data analysis</p><p>online visualization</p>'}
			 
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
			   'debug': settings.DEBUG,
			   'hostname': socket.gethostname(),
			   'visit': Visitor.objects.all().order_by('date')}
	return render(request, 'face.html', context)

