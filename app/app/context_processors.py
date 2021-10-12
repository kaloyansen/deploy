from re import search as rese
import logging
from django.http import HttpResponse
from django.utils import timezone, translation
from app.otverka import safeStyle, flip_language, tracker, get_visitor
from app.encdec import encrypt
from .linked import *

logger = logging.getLogger(__name__)


def get_context(request):
	""" custom context processor delivers real ip, boolean True if unknown user, user language (fr/en))
	in addition it is responsible for the quick message if sended and for the user language if changes """

	ip, nova, lang = tracker(request)
	send = {}
	send['message'] = 'message express'
	send['submit'] = 'go!'
	send['redirect'] = False

	visitor = get_visitor(request)
	
	if "fliplang" in request.POST:
		lang_content = request.POST.get('fliplang', None)
		if lang_content == 'eng':
			""" it happens only when asked for english
			while reading the french manifest
			gonna set manifeste auto appear ! """
			nova = True
			
		lang = flip_language(lang)
		if not visitor:
			x = 0
		else:
			visitor.lang = lang
			visitor.save()

	if "message" in request.POST:
		send['message'] = 'merci'
		send['submit'] = 'sent'		
		
		message_content = request.POST.get("message", None)
		actif = ['^onn[n]+[/]?$', '^off[f]+[/]?$', 'morla', 'base', 'face', 'err[r]+[/]?', 'admin', 'rest', 'news', 'work', 'cv', 'memo/demo', 'memo/spider', 'memo/sun', 'memo/bg']
		
		if not visitor:
			send['message'] = 'error'
			send['submit'] = 'nul'					
		else:
			if message_content == '':
				send['message'] = 'envoyez un message'
				send['submit'] = 'ok'
			else:
				if correspond(actif, message_content): # it was <elif message_content in actif>
					send['redirect'] = '/{}/'.format(message_content)
				else:
					visitor.message = encrypt(message_content)
					visitor.mencrypted = True
					visitor.save()

	send['lang'] = lang
	send['iseng'] = False
	send['lancol'] = 'success'

	if lang == 'fr': send['lancol'] = 'primary'
	elif lang == 'en': send['iseng'] = True
	else: send['lancol'] = 'warning'

	if lang == request.LANGUAGE_CODE:
		x = 0
	else:
		translation.activate(lang)
		request.session[translation.LANGUAGE_SESSION_KEY] = lang

	if send['redirect']:
		send['message'] = 'redirecting'
		send['submit'] = '...'

	context = { # these are accesible from everywhere
		'page_author': 'Kaloyan KRASTEV',
		'page_bg': '/svg/earth.moon.svg',
		'page_brand': '/img/kalodev.png',
		'page_cv': mycv(),
		'page_digitalocean': digitalocean(),
		'page_digitalocean_grand': digitalocean(70),
		'page_django': django(),
		'page_en': send['iseng'],
		'page_github': github(),
		'page_ico': '/favicon.ico',
		'page_lancol': send['lancol'],
		'page_nova': nova,
		'page_not_voted': has_not_voted(request),
		'page_ip': ip,
		'page_linkedin': linkedin(),
		'page_ln_about': linked_about(),
		'page_ln_bg': linked_bg(),
		'page_ln_demo': linked_demo(),
		'page_ln_news': linked_news(),
		'page_ln_sun': linked_sun(),
		'page_ln_work': linked_work(),
		'page_message': send['message'],
		'page_newlang': flip_language(send['lang']),
		'page_oldlang': send['lang'],
		'page_pause': pause(),
		'page_place': 'Grenoble, FRANCE',
		'page_python': python(),
		'page_redirect': send['redirect'],
		'page_stackoverflow': stackoverflow(),
		'page_style': safeStyle('page'),
		'page_submit': send['submit'],
		'page_time': timezone.now(),
		'page_title': 'Kalo KRASTEV',
		'page_tothetop': tothetop('warning'),
		'page_visitor': visitor,
		'page_voted': has_voted(request)}

	return context


def has_not_voted(request): return not has_voted(request)
def has_voted(request):
	visitor = get_visitor(request)
	if not visitor: return False
	return visitor.voted

def set_voted(request):
	visitor = get_visitor(request)
	if not visitor: return False
	visitor.voted = True
	visitor.save()
	return True

def correspond(arrr, messs):
	for mot in arrr:
		if rese(mot, messs): return True
		else: pass
	return False
		
