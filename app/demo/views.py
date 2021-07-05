from django.shortcuts import render

from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import StringIO

import matplotlib.pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np


def demo(request):
    return render(request, 'demo.html')



def plot(request):
    f = plt.figure()
    x = np.arange(10)
    party = ['python', 'javascript', 'c++', 'java', 'php']
    vote = [29, 16, 32, 5, 9]
    explosion = [0.1, 0.1, 0.1, 0.1, 0.1]
    plt.title('vos langages de programmation préférés')
    #plt.xlim(0, 10)
    #plt.ylim(0, 8)
    plt.xlabel('langage de programmation')
    plt.ylabel('')
    #bar1 = plt.bar(x,vote,width=1.0,bottom=0,color='Green',alpha=0.65,label='people')
    bar1 = plt.pie(vote, labels = party, explode = explosion,
				   shadow = True, startangle = 100)
    #plt.legend()

    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
	#plt.savefig('/img/foo.png')
    matplotlib.pyplot.close(f)   
    return response


def pplot(request):
    #x = arange(0, 2*pi, 0.1)
    #s = cos(x)**2
    #plot(x, s)
    plot([1,2,3,4])
    #plot(x)

    xlabel('xlabel(X)')
    ylabel('ylabel(Y)')
    title('Simple Graph!')
    grid(True)

    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), mimetype="image/png")
