from django.shortcuts import render
from django.http import HttpResponse, Http404

#import PIL, PIL.Image

#from matplotlib import pylab
#import matplotlib.pyplot
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg

#from pylab import *
#from io import StringIO

from plotly.offline import plot
import plotly.graph_objects as go
#import numpy as np

from .forms import ProgForm
from .models import dicho, Child, Prog
from app.context_processors import has_not_voted, set_voted

def bg(request):

	context = {
		"graph1": plotter("bg", 1),
		"graph2": plotter("bg", 2) }

	return render(request, 'memo_bg.html', context)


def demo(request):

	if request.method == 'POST':
		postname = request.POST.get("name", None)
		prog = Prog.objects.get(name = postname) 
		form = ProgForm(request.POST, instance = prog)
		if form.is_valid():
			#prog = Prog.objects.get(name = form.cleaned_data["name"])
			prog.code1 += 1
			prog.save()
			set_voted(request)
		else: print(form.errors) #raise Http404
	else: form = ProgForm() # no post data because method == 'GET'
	
	party = ''
	for p in Prog.objects.all():
		party += '{}: {}, '.format(dicho[p.name], p.code1)

	context = {"form": form,
			   "graph": plotter("prog", 0),
			   "party": party,
			   "notvoted": has_not_voted(request),
			   "image": "/img/langage.png"}

	return render(request, 'memo_demo.html', context)

"""
def getPlotData(pk):
	if pk == 1: return getData('avril2021')
	elif pk == 2: return getData('juillet2021')
	else: return getLangageData()


def getLangageData():

	party = {}
	counter = 0
	for x, y in CHOICE:
		party[y] = Langage.objects.filter(name = counter).count() + 10
		counter += 1

	return party


def getData(quand):

	party = {}

	for c in Child.objects.all():
		parent = c.mother
		if parent.name == 'bg':
			if quand == 'avril2021':
				party[c.name] = c.code1
			elif quand == 'juillet2021':
				party[c.name] = c.code2
			else: x = 3

	return party


def printer(request, pk):

	party = getPlotData(pk)
	tt = 'élections bulgares'
	tx = 'bg parlament'
	if pk == 1:
		tt += ' le mai 2021'
		tx += ' in may 2021'
	elif pk == 2:
		tt += ' le juillet 2021'
		tx += ' in july 2021'
	else:
		tt = 'vos langages de programmation préférés'
		tx = 'your favorite proramming languages'

	fig = plt.figure()
	plt.title(tt)
	plt.xlabel(tx)
	plt.ylabel('')
	wedges, texts, autotexts = plt.pie(party.values(),
									   labels = party.keys(),
									   explode = [0.1] * len(party),
									   autopct='%1.1f%%',
									   shadow = True,
									   startangle = 22)
	plt.axis('equal')
	plt.setp(autotexts, size = 11, weight ="bold")
	#plt.legend()

	can = FigureCanvasAgg(fig)
	response = HttpResponse(content_type='image/png')
	#plt.savefig('/img/foo.png')

	#plt.show(block=True)
	can.print_png(response)
	#plt.savefig(response)
	plt.close('all')
	matplotlib.pyplot.close(fig)
	#matplotlib.pyplot.close(can)

	return response
"""


def dbload(table = 'bg', pk = 1):

	colors = []
	labos = []
	valos = []

	objs = 0
	if table == 'bg': objs = Child.objects.all()
	elif table == 'prog': objs = Prog.objects.all()
	else: x = 'go to hell'

	for c in objs: #Child.objects.all():
		#parent = c.mother
		if c.mother.name != table: continue
		if table == 'bg': labos.append(c.name)
		elif table == 'prog': labos.append(dicho[c.name])
		else: x = 'go to hell'
		colors.append(c.color)
		if pk == 0: valos.append(c.code1)
		elif pk == 1: valos.append(c.code1)
		elif pk == 2: valos.append(c.code2)
		else: x = 3  #?

	return colors, labos, valos

def plotter(table, pk, to_graph = True):

	tit = 'élections bulgares'
	if pk == 0:	tit = 'vos langages de programmation préférés'
	elif pk == 1: tit += ' le mai 2021'
	elif pk == 2: tit += ' le juillet 2021'
	else: tit = 'unknown'

	colors, labos, valos = dbload(table, pk)

	pie = go.Pie(labels = labos,
				 values = valos,
				 hole = 0.0,
				 pull = [0.1] * len(labos),
				 sort = False,
				 insidetextorientation = 'radial')

	fig = go.Figure(data = [pie],
					layout = go.Layout(title = tit,
									   showlegend = False))

	fig.update_traces(hoverinfo = 'label+percent',
					  textinfo = 'label+value',
					  textfont_size = 20,
					  marker = dict(colors = colors,
									line = dict(color = 'black',
												width = 2)))

	data = plot(fig, output_type="div")
	#auto_open = False,
	#include_plotlyjs=False,

	if to_graph: return data
	else: return HttpResponse(data)

		



