import socket
from django.utils import timezone
from work.models import Visitor, Page


def fliplanguage(old):
	if old == 'fr': return 'en'
	return 'fr'


def linked(title, color, url, label):
	x = '<a title = "{}"\
	        class = "btn btn-outline-{} rounded-circle"\
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

	visitor = get_visitor(request)
	
	if "fliplang" in request.POST:
		lang_content = request.POST.get('fliplang', None)
		if lang_content == 'eng':
			""" it happens only when asked for english
			while reading the french manifest
			gonna set manifeste auto appear ! """
			nova = True
			
			"""
			post = request.POST.copy() # to make it mutable
			post['fliplang'] = 'en'
			
			request.POST = post # and update original POST in the end
			request.POST.update({'fliplang': 'en'})

			request.query_params._mutable = True
			request.query_params['fliplang'] = 'en' """
			
		lang = fliplanguage(lang)
		if not visitor:
			x = 0
		else:
			visitor.lang = lang
			visitor.save()
		
	if "message" in request.POST:
		send['message'] = 'merci'
		send['submit'] = 'sent'		
		
		message_content = request.POST.get("message", None)
		if not visitor:
			send['message'] = 'error'
			send['submit'] = 'nul'					
		elif message_content == '':
			send['message'] = 'envoyer un message'
			send['submit'] = 'ok'
		else:
			visitor.message = message_content
			visitor.save()

	send['lang'] = lang
	send['iseng'] = False
	send['lancol'] = 'success'

	if lang == 'fr': send['lancol'] = 'primary'
	elif lang == 'en': send['iseng'] = True
	else: send['lancol'] = 'warning'

	return { # these are accesible from everywhere
		'page_title': 'Kaloyan KRASTEV',
		'page_author': 'Kaloyan KRASTEV',
		'page_ico': '/favicon.ico',
		'page_time': timezone.now(),
		'page_place': 'Grenoble, FRANCE',
		'page_nova': nova,
		'page_visitor': visitor,
		'page_not_voted': has_not_voted(request),
		'page_ip': ip,
		'page_oldlang': send['lang'],
		'page_newlang': fliplanguage(send['lang']),
		'page_en': send['iseng'],
		'page_lancol': send['lancol'],
		'page_message': send['message'],
		'page_submit': send['submit'],
		'page_linkedin': linkedin(),
		'page_github': github(),
		'page_digitalocean': digitalocean(request),
		'page_digitalocean_grand': digitalocean(request, 70),
		'page_ln_about': linked("this site", "success", "work/3/", "about"),
		'page_ln_work': linked("work", "secondary", "work/", "work"),
		'page_ln_news': linked("quoi de neuf", "primary", "news/", "news"),
		'page_ln_demo': linked("programming", "danger", "memo/demo/", "language"),
		'page_ln_sun': linked("le système solaire", "warning", "memo/sun/", "solaire"),
		'page_ln_bg': linked("les élections bulgares anticipées", "info", "memo/bg/", "bulgare")
	}


def get_ip(request):
	ip = request.META.get('REMOTE_ADDR')
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for: ip = x_forwarded_for.split(',')[0]

	is_valid = False
	try: # wanna check if the ip is valid
		socket.inet_aton(ip)
		is_valid = True
	except socket.error: x = 0

	return ip, is_valid


def tracker(request):

	ip = 0
	nova = False
	lang = ''
	
	try:
		ip, ip_valid = get_ip(request)
		req_path = request.path
		is_admin = "admin" in '{}'.format(req_path)
		
		if ip_valid:

			visited = Visitor.objects.filter(ip_address=ip).count()
			visitor = 0

			if is_admin: x = 'do not track admin'
			else:				
				visitor, cr = Visitor.objects.get_or_create(ip_address=ip)
				if cr: nova = True
				else: visitor.code += 1
				lang = visitor.lang
				visitor.save()
				
				page, cr = Page.objects.get_or_create(name=req_path,
													  mother=visitor)
				page.date = timezone.now()
				page.code += 1
				page.save()

		else: x = "ip's not valid"
		
	except:	pass

	return ip, nova, lang


def get_visitor(request):
	visitor = False
	try:
		ip, ip_valid = get_ip(request)
		if ip_valid: visitor = Visitor.objects.get(ip_address=ip)
	except: pass
	return visitor

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
