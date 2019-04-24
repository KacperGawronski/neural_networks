#!/usr/bin/env python3
#Propagacja wsteczna
from math import exp

#input
#u[p][3]==1
u=[(0,0,1),(1,0,1),(0,1,1),(1,1,1)]
#nauczyciel
z=[0,1,1,0]

#warunki początkowe:
w=[[0,1,2],[0,1,2]]
s=[0,1,2]
beta=1.0


def f(u):
	return 1.0/(1+exp(-beta*u))
def Df(u):
	return (beta*exp(beta*u))/(exp(beta*u)+1)**2
x=[ [f(sum(w[j][i]*u[p][i] for i in range(len(w[0])))) for j in range(2)] for p in range(4)]
x=[y+[1] for y in x]
print(x)
y=[ f(sum(s[i]*x[p][i] for i in range(3))) for p in range(4) ] 

#Metoda gradientu:
	
