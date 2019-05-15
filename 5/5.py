#!/usr/bin/env python3
#Propagacja wsteczna
from math import exp

#input
#u[p][3]==1
u=[(0,0,1),(1,0,1),(0,1,1),(1,1,1)]
#nauczyciel
z=[0,1,1,0]

#init values
w=[[0,1,2],[0,1,2]]
s=[0,1,2]
beta=1.0
c=0.1
epsilon=0.000001

def f(u):
	return 1.0/(1+exp(-beta*u))
def Df(u):
	return (beta*exp(beta*u))/((exp(beta*u)+1)**2)
def make_x(w):
	tmp=[ [f(sum(w[j][i]*u[p][i] for i in range(len(w[0])))) for j in range(2)] for p in range(4)]
	tmp=[y+[1] for y in tmp]
	return tmp
def y(s,x):
	return [ f(sum(s[i]*x[p][i] for i in range(3))) for p in range(4) ] 

def DE_s(i,s,y,x):
	return sum( ((y[p]-z[p])*Df(sum(s[k]*x[p][k] for k in range(3)))*x[p][i] ) for p in range(4))
def DE_w(i,j,s,y,x,w):
	return sum( ((y[p]-z[p])*Df(sum(s[k]*x[p][k] for k in range(3)))*s[i]*Df(sum(w[i][k]*u[p][k] for k in range(3)))*u[p][j]  ) for p in range(4))

max_diff=1.0
#Metoda gradientu:

while(max_diff>epsilon):
	x_tmp=make_x(w)
	y_tmp=y(s,x_tmp)
	w_new=[ [w[i][j]-c*DE_w(i,j,s,y_tmp,x_tmp,w) for j in range(3)] for i in range(2)]
	s_new=[ (s[i]-c*DE_s(i,s,y_tmp,x_tmp)) for i in range(3) ]
	max_diff=max( max(abs(w_new[i][j]-w[i][j]) for j in range(3) for i in range(2)),max(abs(s_new[i]-s[i]) for i in range(3)))
	s=s_new
	w=w_new
print("s:",s)
for wrow in w: print(wrow)
print(y(s,make_x(w)))
