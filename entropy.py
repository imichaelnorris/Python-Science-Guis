import Tkinter
import pickle
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from Tkinter import Button, Label, StringVar

from collections import defaultdict, Counter

data = []
entropies = []

def update(i):
    data.append(i)
    lastNumbers.set((lastNumbers.get() + str(i))[::5])
    entropyS.set("entropy: " + str(round(entropy(data), 2)))

    entropies.append(entropy(data))
    create_plot()

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())


root = Tkinter.Tk()
root.wm_title("Plotting histogram")

fig = Figure(figsize=(5,4), dpi=100)
a = fig.add_subplot(111)
a.set_xlabel('Side of the Die')
a.set_ylabel('Times Rolled')
a.set_title("Rolling a FDM die")

commandDispatch = lambda i: lambda: update(i)

buttons = [Button(root, text=str(i), command=commandDispatch(i)) for i in range(0, 10)]
buttons[0].grid(row=0, column=0, columnspan=3)
for i in range(3):
    for j in range(3):
        buttons[i*3 + j+1].grid(row=(i+1), column=j)

lastNumbers = StringVar()
entropyS = StringVar()
Label(textvar=lastNumbers).grid(row=4, columnspan=3)
Label(textvar=entropyS).grid(row=5, columnspan=3)

def create_plot():
    a.clear()
    a.set_xlabel('Total Numbers Chosen')
    a.set_ylabel('Shannon Entropy')
    a.set_title("Showing Human Random Choices")

    print data, len(data)
    print entropies
    a.plot(range(len(data)), entropies)
    a.plot(range(len(data)), 3.3)

    canvas.draw()


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


