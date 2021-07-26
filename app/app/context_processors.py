from work.models import Visitor, Page
import socket
from django.utils import timezone

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


def get_context(request):

	#present_date = datetime.datetime.now()
	present_date = timezone.now()
	welcome = 'unknown'

	try:
		"""
		#----- get visitor ip -----#
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		#----- check if ip adress is valid -----#
		try:
			socket.inet_aton(ip)
			ip_valid = True
		except socket.error:
			ip_valid = False
		"""
		ip, ip_valid = get_ip(request)
		
		if ip_valid:
			visited = Visitor.objects.filter(ip_address=ip).count()
			visitor = 0
			if visited == 0: # the first visit creates a new visitor
				visitor = Visitor(ip_address = ip,
								  page_visited = request.path,
								  date = present_date,
								  code = 0)
				visitor.save()
				welcome = 'created'
			else: # more visits modifie the existing visitor
				visitor = Visitor.objects.get(ip_address=ip)
				visitor.date = present_date
				visitor.code += 1
				visitor.page_visited = request.path
				visitor.save()
				welcome = 'updated'

			page = Page(name = request.path,
						date = present_date,
						mother = visitor)
			# the new page is created as a child of the visitor
			page.save()

		else: x = 0 # ip is not valid
	except:	pass

	visit_ip = Visitor.objects.values_list('ip_address', flat=True).distinct().count()
	
	return {
		'page_visit': visit_ip,
		'page_title': 'Kaloyan KRASTEV',
		'page_author': 'Kaloyan KRASTEV',
		'page_ico': '/favicon.ico',
		'page_time': present_date,
		'page_place': 'Grenoble, FRANCE',
		'page_test': welcome,
		'page_ip': request.META['REMOTE_ADDR']
	}

def get_visitor(request):
	visitor = 0
	try:
		ip, ip_valid = get_ip(request)
		if ip_valid: visitor = Visitor.objects.get(ip_address=ip)
	except: pass
	return visitor

def has_not_voted(request):
	visitor = get_visitor(request)
	return not visitor.voted

def set_voted(request):
	visitor = get_visitor(request)
	visitor.voted = True
	visitor.save()
