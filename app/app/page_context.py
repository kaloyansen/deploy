import datetime

def page_param(request):

	now = datetime.datetime.now()

	context = {
        'page_title': 'Kaloyan KRASTEV',
		'page_author': 'Kaloyan KRASTEV',
		'page_ico': '/static/ico/favicon.ico',
		'page_time': now,
		'page_place': 'Grenoble, FRANCE'
	}

	return context

