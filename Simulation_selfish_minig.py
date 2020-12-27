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

            elif(block==1 and random()<gamma):
                R=R+b

            elif(block==0):
                T=T+t

            if(block==0):
                stop=True
    return(R,T)
