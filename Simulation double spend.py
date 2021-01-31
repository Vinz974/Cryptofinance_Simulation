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

def simulation_doublespend(q,n,z,A,v):
    k=1
    R=0
    T=0
    b=6.25
    t0=600
    i=0
    mineur_a=0
    mineur_h=0
    retard=0
    while(i<n):
        if(random()<q):
            i=i+1
            T=T+t0
            mineur_h=0
            mineur_a=0
            retard=0
            while(retard<A and mineur_h<z and mineur_a<z):
                if(random()<q):
                    mineur_a= mineur_a+1
                else:
                    mineur_h = mineur_h+1
                retard=mineur_h-mineur_a
            if(mineur_a==z):
                R=R+b+v
                T=T+t0
            else:
                T=T+t0

        else:
            i=i+1
            T=T+t0
    #print("Rendement: "+ str(R))
    #print("Temps en secondes:"+str(T))
    return((R,T))


def B(a,b):
    B = factorial(a - 1) * factorial(b-1)/factorial(a+b-1)
    return B

#if we assume: A>=2 and A>=z>=1
def attacker_revenue_ratio(z,v,q):
    b=6.25
    t0=600
    #calcul of the binomial coefficient zC(2z-1)
    Cnk = factorial(2*z-1)/( factorial(z-1)*factorial(z) )
    #revenue ratio of the attacker
    Ra = (b/t0)*(2*Cnk*(v/b+1)+2/B(z,z))*pow(q,z+1)

    return Ra



#---------------------------------- Main ----------------------------------

#print("Bienvenue dans la simulation de l'attaque double spend.")
#print("Nous allons commencer par vous demander les valeurs que vou voulez attribuer à chhaque variable:")

# print("Le taux de hachage relatif q (0 < q < 0.5):")
# q1= float(input())
# print("Le nombre de cycle d'attaques n (n > 0):")
# n1=int(input())
# print("Le nombre de confirmations z (z > 0):")
# z1=int(input())
# print("Le seuil de tolerance A ( A > 0):")
# A1=int(input())
# print("Le montant de la double spend v (v > 0):")
# v1=float(input())

# (R,T) = simulation_doublespend(q1,n1,z1,A1,v1)

#(R,T) = simulation_doublespend(0.30,100,6,100,1)
def RMT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()

    #Rendement theorique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=attacker_revenue_ratio(float(valider()[2]),float(valider()[4]),x[i])
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.suptitle('Theoritical dishonest rate of return as a function of q')
    fig.add_subplot(111).plot(x,y)
    fig.legend(["Rendement malhonnete Theorique"],loc='lower right')
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def RMP():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()

    #Rendement pratique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_doublespend(x[i],float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4]))
        y[i]=RT[0]/RT[1]
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.suptitle('Practical dishonest rate of return as a function of q')
    fig.add_subplot(111).plot(x,y)
    fig.legend(["Rendement malhonnete Pratique"],loc='lower right')
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.suptitle('Theoritical honest rate of return as a function of q')
    fig.add_subplot(111).plot(x1,y1)
    fig.legend(["Rendement Honnete"],loc='lower right')
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def RMP_RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()

    #Rendement pratique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_doublespend(x[i],float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4]))
        y[i]=RT[0]/RT[1]
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.suptitle('Comparison of honest and dishonest performance')
    fig.add_subplot(111).plot(x,y,x1,y1)
    fig.legend(["Rendement malhonnete Pratique","Rendement Honnete"],loc='lower right')
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def RMT_RHT():
    if len(Frame2.winfo_children())>1:
        for i in range (len(Frame2.winfo_children())-1):
            Frame2.winfo_children()[1].destroy()

    #Rendement theorique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=attacker_revenue_ratio(float(valider()[2]),float(valider()[4]),x[i])
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.suptitle('Comparison of theoritical honest and dishonest performance')
    fig.add_subplot(111).plot(x,y,x1,y1)
    fig.legend(["Rendement malhonnete Theorique","Rendement Honnete"])
    #fig.add_subplot(111).plot(x1,y1)
    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().grid(row=13,column=1)
    toolbar = NavigationToolbar2Tk(canvas,Frame2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


#Rendement theorique en fonction de z
'''
x1=[0]*30
for i in range(len(x1)):
    x1[i]=i+1
x = np.array(x1)
y=[0]*30
for i in range(len(y)):
    y[i]=attacker_revenue_ratio(x[i],10,0.245)
plt.plot(x,y)
plt.show()
'''

#Rendement pratique en fonction de z
'''
x1=[0]*30
for i in range(len(x1)):
    x1[i]=i+1
x = np.array(x1)
y=np.array(x1)
for i in range(len(y)):
    y[i]=simulation_doublespend(0.3,1000,x[i],3,10)[0]
plt.plot(x,y)
plt.show()
'''

top = tkinter.Tk()

def double():
    doubleSpend=simulation_doublespend(float(valider()[0]),float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4]))
    Res.delete(0,50)
    Res.insert(0,"Gain(BTC): "+str(doubleSpend[0])+" Temps(s): "+ str(doubleSpend[1]))

def valider():
    Q=q.get()
    N=n.get()
    Z=z.get()
    A=a.get()
    V=v.get()
    return([Q,N,Z,A,V])

Frame1=tkinter.Frame(top)
Frame2=tkinter.Frame(top)
Frame1.pack()
Frame2.pack()
lblQ=tkinter.Label(Frame1,text="q")
lblQ.grid(row=1,column=1)
q=tkinter.Entry(Frame1,text="q")
q.insert(0,str(0.2))
q.grid(row=2,column=1)
lblN=tkinter.Label(Frame1,text="n (à 10000 pour des graphiques plus lisibles)")
lblN.grid(row=1,column=2)
n=tkinter.Entry(Frame1,text="n")
n.insert(0,str(10000))
n.grid(row=2,column=2)
lblZ=tkinter.Label(Frame1,text="z")
lblZ.grid(row=3,column=1)
z=tkinter.Entry(Frame1,text="z")
z.insert(0,str(10))
z.grid(row=4,column=1)
lblA=tkinter.Label(Frame1,text="A")
lblA.grid(row=3,column=2)
a=tkinter.Entry(Frame1,text="a")
a.insert(0,str(5))
a.grid(row=4,column=2)
lblV=tkinter.Label(Frame1,text="v")
lblV.grid(row=1,column=3)
v=tkinter.Entry(Frame1,text="v")
v.insert(0,str(10))
v.grid(row=2,column=3)


C=tkinter.Button(Frame1,text="double spend",command =double)
C.grid(row=3,column=3)
Res=tkinter.Entry(Frame1,width=50)
Res.grid(row=4,column=3)
lbl1=tkinter.Label(Frame1,text="")
lbl1.grid(row=5,column=3)

A=tkinter.Button(Frame1, text ="rendement malhonnete pratique", command = RMP)
A.grid(row=6,column=1)
AB=tkinter.Button(Frame1, text ="rendement malhonnete pratique et honnete theorique", command = RMP_RHT)
AB.grid(row=7,column=1)
B1 = tkinter.Button(Frame1, text ="rendement malhonnete theorique", command = RMT)
B1.grid(row=6,column=2)
D=tkinter.Button(Frame1,text="rendement honnete theorique",command =RHT)
D.grid(row=7,column=2)
E=tkinter.Button(Frame1,text="Rendement honnete et malhonnete theorique",command =RMT_RHT)
E.grid(row=6,column=3)

lblQ=tkinter.Label(Frame2,text="Graphique")
lblQ.pack()
def _quit():
    top.quit()     # stops mainloop
    top.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=Frame1, text="Quit here don't close the window", command=_quit)
button.grid(row=7,column=3)
top.mainloop()

