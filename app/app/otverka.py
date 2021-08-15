import socket
import random
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


class rgbColor:

	mini = 0
	maxi = 255
	step = 11
	
	def __init__(self, r = -1, g = -1, b = -1): 
		self.colo = {}
		if r < 0: self.colo['red'] = self.randotdo()
		else: self.colo['red'] = r
		if g < 0: self.colo['green'] = self.randotdo()
		else: self.colo['green'] = g
		if b < 0: self.colo['blue'] = self.randotdo()
		else: self.colo['blue'] = b

	def slide(self, color):
		c = self.colo[color]
		c += self.randotdo(-1 * self.step, self.step)
		if c > self.maxi: c -= self.maxi
		if c < self.mini: c += self.maxi
		self.colo[color] = c
		
	def reload(self):
		self.slide('red')
		self.slide('green')
		self.slide('blue')

	def __str__(self):
		return 'rgb({}, {}, {})'.format(self.colo['red'],
										self.colo['green'],
										self.colo['blue'])

	def randotdo(self, ot = 0, do = 0):
		# lala = lambda: random.randint(0, 255)
		mini = self.mini
		maxi = self.maxi
		if ot != 0: mini = ot
		if do != 0: maxi = do
		return random.randint(mini, maxi)

	def normcol(self, color): return self.colo[color] / self.maxi
	def totnorm(self): return round(self.tot() / 3 / self.maxi, 3)
	def tot(self):
		return self.colo['red'] + self.colo['green'] + self.colo['blue']


		
def safeStyle(title = 'default', force = 0.333):
	cs, created = ColorStyle.objects.get_or_create(title=title)
	fg = bg = 0
	if created: # first time
		bg = rgbColor()
		fg = rgbColor()
	else:
		bg = rgbColor(cs.bred, cs.bgre, cs.bblu)
		bg.reload()
		fg = rgbColor(cs.fred, cs.fgre, cs.fblu)
		fg.reload()

	cont = True
	while cont:
		cont = False

		dired = fg.normcol('red') - bg.normcol('red')
		digre = fg.normcol('green') - bg.normcol('green')
		diblu = fg.normcol('blue') - bg.normcol('blue')

		if abs(dired) < force or\
		   abs(digre) < force or\
		   abs(diblu) < force or\
		   abs(dired) + abs(digre) + abs(diblu) < 3 * force: cont = True

		if cont:
			fg.reload()
			bg.reload()

	cs.bred = bg.colo['red']
	cs.bgre = bg.colo['green']
	cs.bblu = bg.colo['blue']
	cs.fred = fg.colo['red']
	cs.fgre = fg.colo['green']
	cs.fblu = fg.colo['blue']
	cs.save()
	
	return cs
