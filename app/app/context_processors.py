import socket
from django.utils import timezone
from work.models import Visitor, Page


def fliplanguage(old):
	if old == 'fr': return 'en'
	return 'fr'


def get_context(request):

	ip, nova, oldlang = tracker(request)

	if "fliplang" in request.POST:
		oldlang = fliplanguage(oldlang)
		visitor = get_visitor(request)
		if not visitor:
			x = 0
		else:
			visitor.lang = oldlang
			visitor.save()
		
	newlang = fliplanguage(oldlang)

	return { # these are accesible from everywhere
		'page_title': 'Kaloyan KRASTEV',
		'page_author': 'Kaloyan KRASTEV',
		'page_ico': '/favicon.ico',
		'page_time': timezone.now(),
		'page_place': 'Grenoble, FRANCE',
		'page_nova': nova,
		'page_not_voted': has_not_voted(request),
		'page_ip': ip,
		'page_oldlang': oldlang,
		'page_newlang': newlang
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

		else: x = 'ip is not valid'
		
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
