import socket
import logging
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.template import RequestContext
from .otverka import safeStyle, rainbow
from .context_processors import get_visitor
from work.models import Visitor
from memo.plot import animalien

logger = logging.getLogger(__name__)


def handler400(request, e): return lerxxx(400, 'bad request', request)
def handler403(request, e): return lerxxx(403, 'permission denied', request)
def handler404(request, e): return lerxxx(404, 'page not found', request)
def handler418(request): return lerxxx(418, 'i am a teapot', request)
def handler451(request): return lerxxx(451, 'unavailable for legal reasons', request)
def handler500(request): return lerxxx(500, 'internal server error', request)
def handler502(request): return lerxxx(502, 'bad gateway', request)
def handler503(request): return lerxxx(503, 'service unavailable', request)
def lerxxx(code, message, request):
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


def bio(request): return render(request, 'bio.html')
def base(request): return render(request, 'base.html')
def model(request): return render(request, 'model.html')
def bio(request): return render(request, 'bio.html')
def erreur(request): return render(request, 'erreur.html',
								   {'loco': request.path,
									'message': "if you wish you are welcome to send a message express (at the right side of the menu bar) or an e-mail to"})



def mindex(request):
	logger.info(request.path)
	return index(request, 'mindex.html')



def index(request, template_file_name = 'index.html'):
	# logger.info('index')
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	title = {'fr': 'concepteur d??veloppeur d\'applications',
			 'en': 'software design and development'}
	about = {'fr': '<p class = "row">conception d\'applications</p><p class = "row">d??veloppement full stack</p><p class = "row">analyse de donn??es scientifique</p><p class = "row">visualisation en ligne</p>',
			 'en': '<p class = "row">software solutions</p><p class = "row">full stack development</p><p class = "row">scientific data analysis</p><p class = "row">online visualization</p>'}
			 
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
		'techno': 'django, pandas, gnuplot, emacs, oracle, mysql, sql*loader, symfony, vue.js, react.js, angular, CGI, WSGI',
		'num_visits': num_visits
	}
	return render(request, template_file_name, context)


@user_passes_test(lambda u: u.is_superuser)
def face(request):
	for v in Visitor.objects.all(): v.set_bifi()
	context = {'style': safeStyle('zero'),
			   'style1': safeStyle('une'),
			   'style2': safeStyle('deux'),
			   'debug': settings.DEBUG,
			   'hostname': socket.gethostname(),
			   'colcode': [31, 63, 127, 255],
			   'rainbow': rainbow(),
			   'visit': Visitor.objects.all().order_by('-date')}
	return render(request, 'face.html', context)

