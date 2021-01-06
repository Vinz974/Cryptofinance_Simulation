from math import *
from random import *
import numpy as np
import matplotlib.pyplot as plt

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
    #Rendement theorique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=attacker_revenue_ratio(float(valider()[2]),float(valider()[4]),x[i])
    plt.plot(x,y)
    plt.show()

def RMP():
    #Rendement pratique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_doublespend(x[i],float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4]))
        y[i]=RT[0]/RT[1]
    plt.plot(x,y)
    plt.show()

def RHT():
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

def RMP_RHT():
    #Rendement pratique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        RT=simulation_doublespend(x[i],float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4]))
        y[i]=RT[0]/RT[1]
    plt.plot(x,y)
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

def RMT_RHT():
    #Rendement theorique en fonction de q
    x = np.linspace(0, 0.5, 100)
    y=np.linspace(0,0.5,100)
    for i in range(len(y)):
        y[i]=attacker_revenue_ratio(float(valider()[2]),float(valider()[4]),x[i])
    plt.plot(x,y)
    #Rendement honnete theorique en fonction de q
    x1 = np.linspace(0, 0.5, 100)
    y1=np.linspace(0,0.5,100)
    for i in range(len(y1)):
        y1[i]=(x1[i]*6.25)/600
    plt.plot(x1,y1)
    plt.grid(True)
    plt.show()

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
import tkinter

top = tkinter.Tk()

def double():
    print("(Gain, Temps)")
    print(simulation_doublespend(float(valider()[0]),float(valider()[1]),float(valider()[2]),float(valider()[3]),float(valider()[4])))

def valider():
    Q=q.get()
    N=n.get()
    Z=z.get()
    A=a.get()
    V=v.get()
    return([Q,N,Z,A,V])

lblQ=tkinter.Label(top,text="q")
lblQ.pack()
q=tkinter.Entry(top,text="q")
q.pack()
lblN=tkinter.Label(top,text="n (à 10000 pour des graphiques plus lisibles)")
lblN.pack()
n=tkinter.Entry(top,text="n")
n.pack()
lblZ=tkinter.Label(top,text="z")
lblZ.pack()
z=tkinter.Entry(top,text="z")
z.pack()
lblA=tkinter.Label(top,text="A")
lblA.pack()
a=tkinter.Entry(top,text="a")
a.pack()
lblV=tkinter.Label(top,text="v")
lblV.pack()
v=tkinter.Entry(top,text="v")
v.pack()

C=tkinter.Button(top,text="double spend",command =double)
C.pack()
A=tkinter.Button(top, text ="rendement malhonnete pratique", command = RMP)
A.pack()
AB=tkinter.Button(top, text ="rendement malhonnete pratique et honnete theorique", command = RMP_RHT)
AB.pack()
B1 = tkinter.Button(top, text ="rendement malhonnete theorique", command = RMT)
B1.pack()
D=tkinter.Button(top,text="rendement honnete theorique",command =RHT)
D.pack()
E=tkinter.Button(top,text="Rendement honnete et malhonnete theorique",command =RMT_RHT)
E.pack()
top.mainloop()

