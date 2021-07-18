from work.models import Visitor
import socket
import datetime

def get_context(request):

	present_date = datetime.datetime.now()
	welcome = 'unknown'

	try:
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
		#----- check if ip adress is valid -----#
		if ip_valid:

			ref_date_1 = present_date - datetime.timedelta(days=1)
			ref_date_2 = present_date - datetime.timedelta(days=2)

			# if Visitor.objects.filter(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1).count() == 0:
			if Visitor.objects.filter(ip_address=ip).count() == 0:
				new_visitor_infos = Visitor(
					ip_address = ip,
					page_visited = request.path,
					event_date = present_date)
				new_visitor_infos.save()
				welcome = 'created'

			# if Visitor.objects.filter(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1).count() == 1:
			if Visitor.objects.filter(ip_address=ip).count() == 1:
				#visitor_infos_obj = Visitor.objects.get(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1)
				visitor_infos_obj = Visitor.objects.get(ip_address=ip)
				visitor_infos_obj.event_date = present_date
				visitor_infos_obj.save()
				welcome = 'updated'
	except:
		pass

	visit_ip = 0
	ref_date = present_date - datetime.timedelta(minutes=5)
	# visit_ip = Visitor.objects.filter(event_date__gte=ref_date).values_list('ip_address', flat=True).distinct().count()
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

