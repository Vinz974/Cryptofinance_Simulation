#----------------------------------Selfish Mining----------------------------------

from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt

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
    #Rendement malhonnete pratique
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_selfish_mining(float(valider()[1]),x[i],float(valider()[2]))
        y[i]=(RT[0])/(RT[1])
    plt.text(0.1,0.004,"Gamma="+valider()[2])
    plt.plot(x,y)
    plt.grid()
    plt.show()

def RMP_RHT():
    #Rendement malhonnete pratique
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_selfish_mining(float(valider()[1]),x[i],float(valider()[2]))
        y[i]=(RT[0])/(RT[1])
    plt.plot(x,y)
    #Rendement honnete theorique
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

def rendement_theorique(q,gamma):
    p=1-q
    t0=600
    b=6.25
    rendement= (q*b)/t0-(1-gamma)*((p*p*q*(p-q)*b)/(((1+p*q)*(p-q)+p*q)*t0))
    return rendement


#Rendement malhonnete theorique
def RMT():
    x = np.linspace(0, 0.5, 100)
    y =np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=rendement_theorique(x[i],float(valider()[2]))
    plt.plot(x,y)
    plt.show()

def RHT():
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

def RMT_RHT():
    x = np.linspace(0, 0.5, 100)
    y =np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=rendement_theorique(x[i],float(valider()[2]))
    plt.plot(x,y)
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

import tkinter

top = tkinter.Tk()

def selfish():
   print(simulation_selfish_mining(float(valider()[1]),float(valider()[0]),float(valider()[2])))

def valider():
    Q=q.get()
    N=n.get()
    GAMMA=gamma.get()
    return([Q,N,GAMMA])

lblQ=tkinter.Label(top,text="q")
lblQ.pack()
q=tkinter.Entry(top,text="q")
q.pack()
lblN=tkinter.Label(top,text="n (à 10000 pour des graphiques plus lisibles)")
lblN.pack()
n=tkinter.Entry(top,text="n")
n.pack()
lblGAMMA=tkinter.Label(top,text="gamma")
lblGAMMA.pack()
gamma=tkinter.Entry(top,text="gamma")
gamma.pack()

C=tkinter.Button(top,text="selfish mining",command =selfish)
C.pack()
A=tkinter.Button(top, text ="rendement malhonnete pratique", command = RMP)
A.pack()
AB=tkinter.Button(top, text ="rendement malhonnete pratique et honnete theorique", command = RMP_RHT)
AB.pack()
B = tkinter.Button(top, text ="rendement malhonnete theroque", command = RMT)
B.pack()
D=tkinter.Button(top,text="rendement honnete theorique",command =RHT)
D.pack()
E=tkinter.Button(top,text="Rendement honnete et malhonnete theorique",command =RMT_RHT)
E.pack()
top.mainloop()
'''
top = tkinter.Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
A=top.getdouble()
print(A)
top.mainloop()
'''