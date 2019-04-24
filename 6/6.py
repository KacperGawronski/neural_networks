#!/usr/bin/env python3
from math import e
from random import uniform
x=[]
x[0] = [0,0,0,0,0,
    0,1,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0]

x[1]= [0,0,1,1,0,
        0,0,0,1,0,
        0,0,0,1,0,
        0,0,0,0,0,
        0,0,0,0,0]

x[2]= [0,0,0,0,0,
        1,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0]

def f(x):
    return 1/(1+exp(-1*x))
xp=[]
w=[[uniform(-0.5,0.5) for x in range(25)] for y in range(16) ]
b=[uniform(-0.5,0.5) for x in range(16)]
wp=[[uniform(-0.5,0.5) for x in range(16)] for y in range(25)]
bp=[uniform(-0.5,0.5) for x in range(25)]
y=[[f(sum(w[i][j]*x[a][j]+b[i] for j in range(25) )) for i in range(15)] for a in range(3)]
E=1/2
