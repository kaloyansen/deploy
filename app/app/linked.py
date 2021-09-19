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


def digitalocean(request, size = 24):
	return """
	<a title = "digitalocean.com/kaloyansen"
	   class = "btn-outline-info"
       href = "https://www.digitalocean.com/?refcode=ff8b99f4b98b&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
      <img src = "https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg"
           height = "{}mm"
           alt = "DigitalOcean Referral Badge" /></a>
	""".format(size)


def linked_news(): return linked(_("News"), "primary", "news/", _("News"))
def linked_work(): return linked(_("Work"), "info", "work/", _("Work"))
def linked_about(): return linked(_("ThisPage"), "success", "work/3/", _("ThisPage"))
def linked_bg(): return linked(_("PlotBg"), "info", "memo/bg/", _("Bulgarian"))
def linked_demo(): return linked(_("PlotLang"), "danger", "memo/demo/", _("PlotLang"))
def linked_sun(): return linked(_("PlotSun"), "warning", "memo/sun/", _("PlotSun"))
