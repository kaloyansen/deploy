import socket
import random
import math
import logging
from django.utils import timezone
from work.models import Visitor, Mage, ColorStyle

logger = logging.getLogger(__name__)

def tracker(request):

	ip = 0
	nova = False
	lang = ''
	
	try:
		ip, ip_valid = get_ip(request)
		req_path = request.path
		is_admin = "admin" in '{}'.format(req_path)
		
		if ip_valid:

			visitor = 0

			# if is_admin: x = 'do not track admin'
			if False:
				logger.error('False')
			else:
				mage, cr = Mage.objects.get_or_create(name = req_path)
				if cr:
					pass
				else:
					mage.code = mage.code + 1
					mage.date = timezone.now()
				
				visitor, cr = Visitor.objects.get_or_create(ip_address = ip)
				if cr: nova = True
				else: visitor.code += 1
				lang = visitor.lang
				
				visitor.mages.add(mage)
				visitor.save()

		else: logger.error('ip {} is not valid'.format(ip))		
	except:	logger.error('general exception')

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


def gaussian(mean, stdev, x, norm = 255):
	return math.exp(((x - mean) / stdev) ** 2 / -2) * norm


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

	return int(r), int(g), int(b)


def rainbow(stdev = 77, delta = 16, mini = 345, maxi = 678):
	masif = []
	x = mini
	while x < maxi:
		front = rgb(x, stdev, True)
		back = rgb(x, stdev, False)
		costi = ColorStyle(title = 'star {}'.format(x),
						   br = back[0], bg = back[1], bb = back[2],
						   fr = front[0], fg = front[1], fb = front[2])
		masif.append(costi)
		x += delta
		del costi

	return masif
