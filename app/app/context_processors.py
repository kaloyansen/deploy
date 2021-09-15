#from django.conf import settings
#from django.shortcuts import redirect, render
import logging
from django.http import HttpResponse
from django.utils import timezone, translation
from django.utils.translation import ugettext_lazy as _
from app.otverka import safeStyle, flip_language, tracker, get_visitor
from app.encdec import encrypt

logger = logging.getLogger(__name__)

def linked(title, color, url, label):
	x = '<a title = "{}"\
	        class = "btn btn-outline-{} btn-lg rounded-circle"\
	        href = "{}">{}</a>'
	return x.format(title, color, url, label)


def linkedin():
	return """
      <a title = "https://www.linkedin.com/in/kaloyan-k-krastev"
         class = "btn-outline-info"
         href = "https://www.linkedin.com/in/kaloyan-k-krastev/">
        <img src = "https://www.linkedin.com/favicon.ico"
             height = "20mm"
             alt = "linkedin"></a>
	"""

def github():
	return """
      <a title = "https://github.com/kaloyansen/deploy"
         class = "btn-outline-warning"
         href = "https://github.com/kaloyansen/deploy.git">
        <img src = "https://www.github.com/favicon.ico"
             height = "20mm"
             alt = "https://github.com/kaloyansen/deploy"></a>
	"""


"""
def digitalocean(request, size = 24):
	return render(request,
				  'digitalocean.html',
				  {'size': size})
"""

def pause():
	return """
<div class = "container-fluid">
  <div class = "row" id = "pause">
    <br class = "clear" />
  </div>
  <div class = "row" id = "pause">
    <br class = "clear" />
  </div>
</div>
	"""


def digitalocean(request, size = 24):
	return """
	<a title = "digitalocean.com/kaloyansen"
	   class = "btn-outline-info"
       href = "https://www.digitalocean.com/?refcode=ff8b99f4b98b&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
      <img src = "https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg"
           height = "{}mm"
           alt = "DigitalOcean Referral Badge" /></a>
	""".format(size)


	
	
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
		actif = ['on', 'off', 'morla', 'base', 'face', 'err', 'admin', 'rest', 'news', 'work', 'cv', 'memo/demo', 'memo/spider', 'memo/sun', 'memo/bg']
		
		if not visitor:
			send['message'] = 'error'
			send['submit'] = 'nul'					
		elif message_content == '':
			send['message'] = 'envoyez un message'
			send['submit'] = 'ok'
		elif message_content in actif:
			send['redirect'] = '/{}'.format(message_content)
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
		'page_brand': '/img/kalodev.png',
		'page_digitalocean': digitalocean(request),
		'page_digitalocean_grand': digitalocean(request, 70),
		'page_en': send['iseng'],
		'page_github': github(),
		'page_ico': '/favicon.ico',
		'page_lancol': send['lancol'],
		'page_nova': nova,
		'page_not_voted': has_not_voted(request),
		'page_ip': ip,
		'page_linkedin': linkedin(),
		'page_ln_news': linked(_("News"), "primary", "news/", _("News")),
		'page_ln_work': linked(_("Work"), "info", "work/", _("Work")),
		'page_ln_about': linked(_("ThisPage"), "success", "work/3/", _("ThisPage")),
		'page_ln_bg': linked(_("PlotBg"), "info", "memo/bg/", _("Bulgarian")),
		'page_ln_demo': linked(_("PlotLang"), "danger", "memo/demo/", _("PlotLang")),
		'page_ln_sun': linked(_("PlotSun"), "warning", "memo/sun/", _("PlotSun")),
		'page_message': send['message'],
		'page_newlang': flip_language(send['lang']),
		'page_oldlang': send['lang'],
		'page_pause': pause(),
		'page_place': 'Grenoble, FRANCE',
		'page_redirect': send['redirect'],
		'page_style': safeStyle('page'),
		'page_submit': send['submit'],
		'page_time': timezone.now(),
		'page_title': 'Kaloyan KRASTEV',
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
