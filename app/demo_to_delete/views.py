from django.shortcuts import render
from django.http import HttpResponse

from matplotlib import pylab
from pylab import *
#import PIL, PIL.Image
from io import StringIO
from plotly.offline import plot
import plotly.graph_objects as go
import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
#import numpy as np

from .forms import LangageForm
from .models import Langage, CHOICE, Child


def bg(request):

	context = {
		'graph1': return_graph(1),
		'graph2': return_graph(2)}

	return render(request, 'bg.html', context)


def demo(request):
	form = LangageForm()
	langage = 0
	#request.POST.getlist("name")
	if request.method == 'POST':
		form = LangageForm(request.POST)
		if form.is_valid():
			langage = Langage( name = form.cleaned_data["name"] )
			langage.save()
		else: print('too bad - form is not valid')

	arty = getLangageData();
	party = ''
	for k in arty.keys(): party += '{}: {}, '.format(k, arty[k])

	context = {"form": form,
			   "langage": langage,
			   "party": party,
			   'image': '/img/langage.png'
			   }

	return render(request, 'demo.html', context)


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


def return_graph(pk):

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

	colors = ['blue', 'cyan', 'gold', 'red', 'magenta', 'black']
	labos = []
	valos = []

	for la in party.keys(): # this is very stupid
		labos.append('{}'.format(la))
		valos.append('{}'.format(party[la]))

	pie = go.Pie(labels = labos,
				 values = valos,
				 pull = [0.1] * len(party),
				 insidetextorientation = 'radial')

	fig = go.Figure(data = [pie], layout = go.Layout(title = tt))
	fig.update_traces(hoverinfo = 'label+percent',
					  textinfo = 'value',
					  textfont_size = 20,
					  marker = dict(colors = colors,
									line = dict(color = 'cyan', width = 1)))

	data = plot(fig, auto_open = False, output_type="div")

	return data


