import Tkinter
import pickle
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from collections import defaultdict
root = Tkinter.Tk()
root.wm_title("Plotting histogram")

fig = Figure(figsize=(5,4), dpi=100)
a = fig.add_subplot(111)
a.set_xlabel('Side of the Die')
a.set_ylabel('Times Rolled')
a.set_title("Rolling a FDM die")

def get_min(b):
    return 0

def get_max(b):
    b = max(b)
    v = [5,10,20,30,40,50,75,100]
    for i,j in enumerate(v):
        if (b < j):
            if j == 100:
                break
            return v[i+1]
    return b + 25

def create_plot():
    a.clear()
    a.set_xlabel('Side of the Die')
    a.set_ylabel('Times Rolled')
    a.set_title("Rolling a FDM die")
    a.set_xticks(range(1,7))

    n = range(1, 7)
    bins = [data[i] for i in n]

    rolls = float(sum(bins))
    average = rolls / 6.0
    stdev = (sum([(i - average)**2 for i in bins]))**.5

    total_rolls.set(str(sum(bins)))

    mi = get_min(bins)
    ma = get_max(bins)
    if ma == 5:
        step = 1
    elif ma < 50:
        step = 5
    else:
        step = 10

    a.bar(n, bins)
    a.plot([1, 7], [average]*2, lw=2, color="green")
    a.plot([1, 7], [average-stdev]*2, '--', lw=2, color="red")
    a.plot([1, 7], [average+stdev]*2, '--', lw=2, color="red")
    a.yaxis.set_ticks(np.arange(mi, ma, step))
    canvas.draw()

def open_file():
    try:
        x = pickle.load(open("file.pickle", 'rb'))
        if type(x) == dict:
            return defaultdict(lambda: 0, x)
    except:
        pass
    return defaultdict(lambda: 0)

def save():
    d = dict(data)
    pickle.dump(d, open("file.pickle", "wb"))

global data
data = open_file()

def f(x, sign):
    '''handle data receive changes'''
    global data
    if sign == '+':
        data[x] += 1
    elif sign == '-':
        data[x] = max(data[x]-1, 0)

    create_plot()
    save()

def inc(x):
    return lambda: f(x, '+')

def dec(x):
    return lambda: f(x, '-')

labels = [Tkinter.Label(root, text=str(i)).grid(row=i-1,column=0) for i in range(1, 7)]
buttons_inc = [Tkinter.Button(root, text="+", command=inc(i)).grid(row=i-1, column=1) for i in range(1,7)]
buttons_dec = [Tkinter.Button(root, text="-", command=dec(i)).grid(row=i-1, column=2) for i in range(1,7)]

total_label = Tkinter.Label(root, text="Rolls:")
total_label.grid(row=6, column=0)

total_rolls = Tkinter.StringVar()
total_rolls_label = Tkinter.Label(root, textvariable=total_rolls)
total_rolls_label.grid(row=6, column=1)

frame = Tkinter.Frame(root)
frame.grid(row=0, column=3, rowspan=8)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.show()
canvas.get_tk_widget().pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, frame)
toolbar.update()
canvas._tkcanvas.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)

def on_key_event(event):
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)

create_plot()

def _quit():
    root.quit()
    root.destroy()

root.mainloop()
