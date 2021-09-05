# import sys

# sys.path.insert(0, '/home/django/deploy/app/venv/lib/python3.8/site-packages')
#from plotly.offline import plot
# import plotly.graph_objects as go

from django.shortcuts import render

from .forms import ProgForm
from .models import dicho, Prog
from .plot import solar_system, plotter, animalien
from app.context_processors import set_voted

def bg(request):
	redirection = True
	redire = '/memo/bg/bg/bg'
	stay_time = 34 # sec
	loop = stay_time * 1.8
	dim = 44
	return render(request, 'memo_bg.html', {'graph': animalien(loop, dim),
											'graph1': plotter('bg', 1),
											'graph2': plotter('bg', 2),
											'disco': redirection,
											'after': stay_time * 1000,
											'red': redire})


def bgbgbg(request):
	redirection = True
	redire = '/memo/bg'
	stay_time = 15 # min
	return render(request, 'memo_bg.html', {'graph': plotter('bg', 3),
											'graph1': plotter('bg', 1),
											'graph2': plotter('bg', 2),
											'disco': redirection,
											'after': stay_time * 60000,
											'red': redire})


def sun(request):
	context = {'graph': solar_system()}
	return render(request, 'memo_sun.html', context)


def spider(request):
	context = {'graph': animalien()}
	return render(request, 'memo_spider.html', context)


def demo(request):

	form = ProgForm()
	if request.method == 'POST':
		if 'name' in request.POST:
			postname = request.POST.get("name", None)
			prog = Prog.objects.get(name = postname)
			form = ProgForm(request.POST, instance = prog)
			if form.is_valid():
				#prog = Prog.objects.get(name = form.cleaned_data["name"])
				prog.code1 += 1
				prog.save()
				set_voted(request)
			else: print(form.errors) #raise Http404
		else: x = 0 # another post
	else: x = 0 # no post data 

	party = ''
	for p in Prog.objects.all():
		party += '{}: {}, '.format(dicho[p.name], p.code1)

	context = {"form": form,
			   "graph": plotter("prog", 0),
			   "party": party,
			   "image": "/img/langage.png"}
	return render(request, 'memo_demo.html', context)


