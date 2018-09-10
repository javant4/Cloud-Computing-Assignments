import numpy as np
from numpy import linspace
from math import sqrt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import os, time, glob

#calculate quadratic formula

#def quadratic_formula(a, b, c):
#    pm = np.array([1, -1])
#    return x1, x2 = (-b + pm * sqrt(abs(b**2 - (4 * a * c))))/(2*a)

def calc(a, b, c):
    """Return filename of plot of the damped_vibration function."""
    pm = np.array([1,-1])
    x1, x2 = (-b + pm * sqrt(abs(b**2 - (4 * a * c))))/(2*a)
    print(os.getcwd())
    x = linspace(-100, 100)
    y = (a * x**2) + (b * x) + c
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(x, y)
    plt.title('x1=%g, x2=%g' % (x1, x2))
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    plotfile = os.path.join('static/static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile

if __name__ == '__main__':
    print(calc(1, 2, 4))