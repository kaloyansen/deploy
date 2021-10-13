import random
import math
import numpy as np

import plotly.express as plx
import plotly.graph_objects as go
from plotly.offline import plot

from django.http import HttpResponse, Http404

from .models import Child, Prog, dicho


""" le système solaire """


def spheres(size, clr, dist = 0): 
    
	# Set up 100 points. First, do angles
	theta = np.linspace(0,2 * np.pi, 100)
	phi = np.linspace(0, np.pi, 100)

	# Set up coordinates for points on the sphere
	x0 = dist + size * np.outer(np.cos(theta), np.sin(phi))
	y0 = size * np.outer(np.sin(theta), np.sin(phi))
	z0 = size * np.outer(np.ones(100), np.cos(phi))

	# Set up trace
	trace = go.Surface(x = x0,
					   y = y0,
					   z = z0,
					   colorscale = [[0, clr],
									 [1, clr]])
	trace.update(showscale = False)

	return trace


def orbits(dist, offset = 0, clr = 'white', wdth = 2): 

	# Initialize empty lists for eac set of coordinates
	xcrd = []
	ycrd = []
	zcrd = []

	# Calculate coordinates
	for i in range(0, 361):
		xcrd = xcrd + [(round(np.cos(math.radians(i)), 5)) * dist + offset]
		ycrd = ycrd + [(round(np.sin(math.radians(i)), 5)) * dist]
		zcrd = zcrd + [0]

	trace = go.Scatter3d(x = xcrd,
						 y = ycrd,
						 z = zcrd,
						 marker = dict(size = 0.1),
						 line = dict(color = clr,
									 width = wdth))
	return trace


def annot(xcrd, zcrd, txt, xancr = 'center'):
	strng = dict(showarrow = False,
				 x = xcrd,
				 y = 0,
				 z = zcrd,
				 text = txt,
				 xanchor = xancr,
				 font = dict(color = 'white',
							 size = 12))
	return strng


def solar_system():
	# Note, true diameter of the Sun is 1,392,700km.
	# Reduced it for better visualization
	diameter_km = [200000, 4878, 12104, 12756, 6787, 142796, 120660, 51118, 48600]
	diameter = [((i / 12756) * 2) for i in diameter_km]
	distance_from_sun = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1]

	# Create spheres for the Sun and planets
	trace0 = spheres(diameter[0], '#ffff00', distance_from_sun[0]) # Sun
	trace1 = spheres(diameter[1], '#87877d', distance_from_sun[1]) # Mercury
	trace2 = spheres(diameter[2], '#d23100', distance_from_sun[2]) # Venus
	trace3 = spheres(diameter[3], '#325bff', distance_from_sun[3]) # Earth
	trace4 = spheres(diameter[4], '#b20000', distance_from_sun[4]) # Mars
	trace5 = spheres(diameter[5], '#ebebd2', distance_from_sun[5]) # Jupyter
	trace6 = spheres(diameter[6], '#ebcd82', distance_from_sun[6]) # Saturn
	trace7 = spheres(diameter[7], '#37ffda', distance_from_sun[7]) # Uranus
	trace8 = spheres(diameter[8], '#2500ab', distance_from_sun[8]) # Neptune

	# Set up orbit traces
	trace11 = orbits(distance_from_sun[1]) # Mercury
	trace12 = orbits(distance_from_sun[2]) # Venus
	trace13 = orbits(distance_from_sun[3]) # Earth
	trace14 = orbits(distance_from_sun[4]) # Mars
	trace15 = orbits(distance_from_sun[5]) # Jupyter
	trace16 = orbits(distance_from_sun[6]) # Saturn
	trace17 = orbits(distance_from_sun[7]) # Uranus
	trace18 = orbits(distance_from_sun[8]) # Neptune

	# Use the same to draw a few rings for Saturn
	trace21 = orbits(23, distance_from_sun[6], '#827962', 3) 
	trace22 = orbits(24, distance_from_sun[6], '#827962', 3) 
	trace23 = orbits(25, distance_from_sun[6], '#827962', 3)
	trace24 = orbits(26, distance_from_sun[6], '#827962', 3) 
	trace25 = orbits(27, distance_from_sun[6], '#827962', 3) 
	trace26 = orbits(28, distance_from_sun[6], '#827962', 3)

	layout = go.Layout(title = 'Solar System',
					   showlegend = False,
					   margin = dict(l = 0, r = 0, t = 0, b = 0),
					   #paper_bgcolor = 'black',
					   scene = dict(
						   xaxis = dict(title = 'Distance from the Sun', 
										titlefont_color = 'black', 
										range = [-7000, 7000], 
										backgroundcolor = 'black',
										color = 'black',
										gridcolor = 'black'),
						   yaxis = dict(title = 'Distance from the Sun',
										titlefont_color = 'black',
										range = [-7000, 7000],
										backgroundcolor = 'black',
										color = 'black',
										gridcolor = 'black'),
						   zaxis = dict(title = '', 
										range = [-7000, 7000],
										backgroundcolor = 'black',
										color = 'white', 
										gridcolor = 'black'),
						   annotations  =  [
							   annot(distance_from_sun[0],
									 40,
									 'Sun',
									 xancr = 'left'),
							   annot(distance_from_sun[1], 5, 'Mercury'),
							   annot(distance_from_sun[2], 9, 'Venus'),
							   annot(distance_from_sun[3], 9, 'Earth'),
							   annot(distance_from_sun[4], 7, 'Mars'),
							   annot(distance_from_sun[5], 30, 'Jupyter'),
							   annot(distance_from_sun[6], 28, 'Saturn'),
							   annot(distance_from_sun[7], 20, 'Uranus'),
							   annot(distance_from_sun[8], 20, 'Neptune')]
					   ))

	fig = go.Figure(data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace21, trace22, trace23, trace24, trace25, trace26],
					layout = layout)

	#fig.show()
	#fig.write_html("Solar_system.html")

	return plot(fig, output_type = 'div')


def rod(ot = -23, do = 23): return random.randint(ot, do)


def randarray(dim):
	j = 0
	xarr = []
	while j < dim:
		xarr.append(rod())
		j = j + 1

	xarr.append(xarr[0])
	return xarr


def rotation(kol):
	if kol == '-': return '\\'
	elif kol == '\\': return '|'
	elif kol == '|': return '/'
	elif kol == '/': return '-'
	else: return '-'
	
def randoframe(loop, dim):
	rf = []
	loop = int(loop)
	treta = loop / 3
	kolelo = '-'
	while loop > 1:
		kolelo = rotation(kolelo)
		texte = "data load ({})".format(kolelo)
		if loop < 2 * treta: texte = "process data ({})".format(kolelo)
		if loop < treta: texte = "iteration {}".format(loop)
		rf.append(go.Frame(data = [go.Scatter(x = randarray(dim),
											  y = randarray(dim))],
						   layout = go.Layout(title_text = texte)))
		loop -= 1

	texte = "plot ..."
	rf.append(go.Frame(data = [go.Scatter(x = randarray(dim),
										  y = randarray(dim))],
					   layout = go.Layout(title_text = texte)))

	return rf


def animalien(loop = 100, dim = 33):
	fig = go.Figure(
		data = [go.Scatter(x = randarray(dim),
						   y = randarray(dim))],
		layout = go.Layout(
			title_text = "lienar iteration",
			paper_bgcolor = 'rgb(246, 246, 246)',
			plot_bgcolor = 'rgb(31, 31, 31)',
			xaxis = dict(range = [-50, 50], autorange = False, showgrid = False, zeroline = False, visible = False),
			yaxis = dict(range = [-50, 50], autorange = False, showgrid = False, zeroline = False, visible = False),
			font = dict(
				family = "Courier New, monospace",
				color = "#008800",
				size = 12
            )),
			# title = "Start Title",
			# updatemenus = [dict(type = "buttons",
			# 					buttons = [dict(label = "Play",
			# 									method = "animate",
			# 									args = [None])])]),
		frames = randoframe(loop, dim))

	return plot(fig, output_type = 'div')



def dbload(table = 'bg', pk = 1):

	colors = []
	labos = []
	valos = []

	objs = 0
	if table == 'bg': objs = Child.objects.all()
	elif table == 'prog': objs = Prog.objects.all()
	else: x = 'go to hell'

	for c in objs:
		if c.mother.name != table: continue
		if pk == 0:
			# if c.code1 < 1: continue
			valos.append(c.code1)
		elif pk == 1:
			if c.code1 < 1: continue # do not want
			else: valos.append(c.code1)
		elif pk == 2:
			if c.code2 < 1: continue # to plot parties
			else: valos.append(c.code2)
		elif pk == 3:
			if c.code3 < 1: continue # without a deputy
			else: valos.append(c.code3)
		else: x = 4 #?
		
		if table == 'bg': labos.append(c.name)
		elif table == 'prog': labos.append(dicho[c.name])
		else: x = 'go to hell'
		colors.append(c.color)

	return colors, labos, valos


def plotter(table, pk, to_graph = True):

	tit = 'les élections'
	if pk == 0:	tit = 'vos langages de programmation préférés'
	elif pk == 1: tit += ' parlementaires l\'avril 2021'
	elif pk == 2: tit += ' anticipées le juillet 2021'
	elif pk == 3: tit += ' anticipées le november 2021'
	else: tit = 'unknown'

	colors, labos, valos = dbload(table, pk)

	pie = go.Pie(labels = labos,
				 values = valos,
				 hole = 0.0,
				 pull = [0.134] * len(labos),
				 #autopct='%1.1f%%',
				 #startangle = 90,
				 sort = False,
				 insidetextorientation = 'radial')

	fig = go.Figure(data = [pie],
					#figsize = (4, 3),
					layout = go.Layout(title = tit,
									   showlegend = False))

	fig.update_traces(hoverinfo = 'label+percent',
					  textinfo = 'label+value',
					  textfont_size = 20,
					  marker = dict(colors = colors,
									line = dict(color = 'black',
												width = 2)))

	data = plot(fig,
				output_type = "div")
	#auto_open = False,
	#include_plotlyjs=False,

	#fig.write_html("/home/kalo/public_html/deploy/app/plotter.html")

	if to_graph: return data
	return HttpResponse(data)


def gapminder(loop, dim):
	fig = plx.scatter(plx.data.gapminder(),
					  x = "pop",
					  y = "lifeExp",
					  animation_frame = "year",
					  animation_group = "country",
					  size = "gdpPercap",
					  color = "continent",
					  hover_name = "country",
					  log_x = True,
					  size_max = 45,
					  range_x = [10000, 10000000000],
					  range_y = [25, 90])
	return plot(fig,
				output_type = 'div')

	

