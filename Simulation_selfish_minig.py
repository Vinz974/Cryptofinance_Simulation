#----------------------------------Selfish Mining----------------------------------

from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter

global top
def simulation_selfish_mining(n,q,gamma):
    R=0
    C=0
    b=6.25
    T=0
    t=600
    f=60/26900
    i=0
    block=0
    stop=False

    while(i<n):
        i=i+1
        stop=False
        block=0

        while(stop==False):

            while(random()<q):
                block=block+1
                T=T+t

            if(block>=2):
                block=block-2
                R=R+2*b

            elif(block==1 and random()>q):
                if(random()<gamma):
                    R=R+b
                    block=0
                else:
                    block=0

            elif(block==0):
                T=T+t

            if(block==0):
                stop=True
    return(R,T)

def RMP():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    #Rendement malhonnete pratique
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_selfish_mining(float(valider()[1]),x[i],float(valider()[2]))
        y[i]=(RT[0])/(RT[1])
    plt.text(0.1,0.004,"Gamma="+valider()[2])
    #plt.plot(x,y)
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).plot(x,y)
    fig.suptitle("Rendement Malhonnete Pratique")
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    #plt.grid()
    #plt.show()

def RMP_RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    #Rendement malhonnete pratique
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_selfish_mining(float(valider()[1]),x[i],float(valider()[2]))
        y[i]=(RT[0])/(RT[1])
    #plt.plot(x,y)
    #Rendement honnete theorique
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).plot(x,y,x1,y1)
    fig.legend(["Rendement malhonnete Pratique","Rendement Honnete"])
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #plt.plot(x1,y1)
    #plt.grid(True)
    #plt.show()


def rendement_theorique(q,gamma):
    p=1-q
    t0=600
    b=6.25
    rendement= (q*b)/t0-(1-gamma)*((p*p*q*(p-q)*b)/(((1+p*q)*(p-q)+p*q)*t0))
    return rendement


#Rendement malhonnete theorique
def RMT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    x = np.linspace(0, 0.5, 100)
    y =np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=rendement_theorique(x[i],float(valider()[2]))
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).plot(x,y)
    fig.suptitle("Rendement Malhonnete Theorique")
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #plt.plot(x,y)
    #plt.show()

def RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    #plt.plot(x1,y1)
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).plot(x1,y1)
    fig.suptitle("Rendement Honnete")
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #plt.grid(True)
    #plt.show()

def RMT_RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    x = np.linspace(0, 0.5, 100)
    y =np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=rendement_theorique(x[i],float(valider()[2]))
    #plt.plot(x,y)
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).plot(x,y,x1,y1)
    fig.legend(["Rendement malhonnete Theorique","Rendement Honnete"])
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #plt.plot(x1,y1)
    #plt.grid(True)
    #plt.show()


top = tkinter.Tk()
top.wm_title("Simulation selfish Mining")
def selfish():
    selfish=simulation_selfish_mining(float(valider()[1]),float(valider()[0]),float(valider()[2]))
    Res.delete(0,50)
    Res.insert(0,"Gain(BTC): "+str(selfish[0])+" Temps(s): "+ str(selfish[1]))

def valider():
    Q=q.get()
    N=n.get()
    GAMMA=gamma.get()
    return([Q,N,GAMMA])

Frame1=tkinter.Frame(top)
Frame2=tkinter.Frame(top)
Frame1.pack()
Frame2.pack()
lblQ=tkinter.Label(Frame1,text="q")
lblQ.grid(row=1,column=1)
q=tkinter.Entry(Frame1,text="q")
q.insert(0,str(0.2))
q.grid(row=2,column=1)
lblN=tkinter.Label(Frame1,text="                         n (à 10000 pour des graphiques plus lisibles)                      ")
lblN.grid(row=1,column=2)
n=tkinter.Entry(Frame1,text="n")
n.insert(0,str(10000))
n.grid(row=2,column=2)
lblGAMMA=tkinter.Label(Frame1,text="gamma")
lblGAMMA.grid(row=3,column=1)
gamma=tkinter.Entry(Frame1,text="gamma")
gamma.insert(0,str(0.2))
gamma.grid(row=4,column=1)

Res=tkinter.Entry(Frame1,width=50)
Res.grid(row=4,column=2)
lbl1=tkinter.Label(Frame1,text="")
lbl1.grid(row=5,column=1)

C=tkinter.Button(Frame1,text="selfish mining",command =selfish)
C.grid(row=3,column=2)
A=tkinter.Button(Frame1, text ="rendement malhonnete pratique", command = RMP)
A.grid(row=6,column=1)
AB=tkinter.Button(Frame1, text ="rendement malhonnete pratique et honnete theorique", command = RMP_RHT)
AB.grid(row=7,column=1)
B = tkinter.Button(Frame1, text ="rendement malhonnete theroque", command = RMT)
B.grid(row=6,column=2)
D=tkinter.Button(Frame1,text="rendement honnete theorique",command =RHT)
D.grid(row=7,column=2)
E=tkinter.Button(Frame1,text="Rendement honnete et malhonnete theorique",command =RMT_RHT)
E.grid(row=8,column=1)
lbl3=tkinter.Label(Frame1,text="")
lbl3.grid(row=9,column=1)
lblQ=tkinter.Label(Frame2,text="Graphique")
lblQ.pack()
#lbl2=tkinter.Label(Frame1,text="Graphique")
#lbl2.grid(row=10,column=1)
def _quit():
    top.quit()     # stops mainloop
    top.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=Frame1, text="Quit here don't close the window", command=_quit)
button.grid(row=8,column=2)

top.mainloop()