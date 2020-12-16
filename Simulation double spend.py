from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
'''
print("Bienvenue dans la simulation de l'attaque double spend.")
print("Nous allons commencer par vous demander les valeurs que vou voulez attribuer à chhaque variable:")

print("Le taux de hachage relatif q (0 < q < 0.5):")

q1= float(input())

print("Le nombre de cycle d'attaques n (n > 0):")

n1=int(input())

print("Le nombre de confirmations z (z > 0):")

z1=int(input())

print("Le seuil de tolerance A ( A > 0):")

A1=int(input())

print("Le montant de la double spend v (v > 0):")
v1=float(input())
'''

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

