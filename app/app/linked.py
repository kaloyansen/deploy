from django.utils.translation import ugettext_lazy as _


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


def tothetop(style = 'info'):
	return """
<a class = "btn btn-outline-{}"
   href = "#"
   data-toggle = "popover"
   title = "{}"
   data-content = "the content inside">{}</a>
	""".format(style, _("ToTheTop"), _("ToTheTop"))


def linked_news():  return linked(_("News"),     'news/',      'primary')
def linked_work():  return linked(_("Work"),     'work/',      'info')
def linked_about(): return linked(_("ThisPage"), 'work/3/',    'success')
def linked_bg():    return linked(_("PlotBg"),   'memo/bg/',   'info', _("Bulgarian"))
def linked_demo():  return linked(_("PlotLang"), 'memo/demo/', 'danger')
def linked_sun():   return linked(_("PlotSun"),  'memo/sun/',  'warning')
def linked(title, url, style, label = False):
	if not label: label = title
	return """
<a title = "{}"
   class = "btn btn-outline-{} btn-lg rounded-circle"
   href = "{}">{}</a>
	""".format(title, style, url, label)


def python(): return limage('python',
							'https://www.python.org',
							'/static/svg/python.svg')
def django(): return limage('django',
							'https://www.djangoproject.com',
							'/static/svg/django.svg')
def mycv(): return limage('curriculum vitæ',
						  '/cv',
						  '/static/svg/cv.svg')
def stackoverflow(): return limage('stackoverflow',
								   'https://stackoverflow.com/users/3566444/morla',
								   '/static/ico/stackoverflow.ico')
def linkedin(): return limage('linkedin',
							  'https://www.linkedin.com/in/kaloyan-k-krastev',
							  '/static/ico/linkedin.ico')
def github(): return limage('github',
							'https://github.com/kaloyansen/deploy.git',
							'/static/svg/github.svg')
#							'/static/ico/github.ico')
def digitalocean(size = 24): return limage('digitalocean',
										   'https://www.digitalocean.com/?refcode=ff8b99f4b98b&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge',
										   '/static/svg/digital.svg',
										   '{}mm'.format(size))
def limage(title, url, source, height = '20mm', style = 'info'):
	return """
<a title = "automatic generation"
   class = "btn-outline-{}"
   href = "{}">
  <img title = "{}"
	   src = "{}"
       height = "{}"
       alt = "image not found"></a>
	""".format(style, url, title, source, height)
