import socket
import random
import math
from work.models import Visitor, Page, ColorStyle


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


def flip_language(old):
	if old == 'fr': return 'en'
	return 'fr'


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


def safeStyle(title = 'default', force = 0.333):

	cs, created = ColorStyle.objects.get_or_create(title=title)
	cs.fill()
	while cs.is_not_contrast(force): cs.fill()

	cs.save()	
	return cs


def gaussian(mean, stdev, x, norm = 255): return math.exp(((x - mean) / stdev) ** 2 / -2) * norm
def rgb(x, stdev = 1, inverse = False):

	r = gaussian(666, stdev, x)
	g = gaussian(543, stdev, x)
	b = gaussian(456, stdev, x)

	norm = 255
	den = norm / 2
	if inverse:
		if r > den: r -= den
		else: r += den
		if g > den: g -= den
		else: g += den
		if b > den: b -= den
		else: b += den

	return 'rgb({}, {}, {})'.format(int(r), int(g), int(b))


def rainbow(stdev = 77, delta = 16, mini = 345, maxi = 678):
	masif = []
	x = mini
	while x < maxi:
		txt = rgb(x, stdev)
		txti = rgb(x, stdev, True)
		print(x, txt)
		masif.append('background-color:{}; color:{};'.format(txt, txti))
		x += delta

	return masif
