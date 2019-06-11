#!/usr/bin/env python3
from math import exp
from random import uniform
x=[]
x.append([0,0,0,0,0,
    0,1,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0])

x.append([0,0,1,1,0,
        0,0,0,1,0,
        0,0,0,1,0,
        0,0,0,0,0,
        0,0,0,0,0])

x.append([0,0,0,0,0,
        1,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0])
w=[[uniform(-0.5,0.5) for i in range(25)] for j in range(16)]
wp=[[uniform(-0.5,0.5) for i in range(16)] for k in range(25)]
bp=[uniform(-0.5,0.5) for k in range(25)]
b=[uniform(-0.5,0.5) for i in range(16)]
#const
beta = 1
epsilon = 0.001
c=0.8
def f(x):
    return 1/(1+exp(-beta*x))
def Df(x):
	f_temp=f(x)
	return f_temp*(1-f_temp)
#y
def enkoder(x,i):
	return f(sum(w[i][j]*x[j]+b[i] for j in range(25)))
#x
def dekoder(y,k):
	return f(sum(wp[k][i]*y[i]+bp[k] for i in range(16)))


def stop(w,w_new,wp,wp_new):
	for pair in zip(w,w_new):
		for p in zip(pair[0],pair[1]):
			if abs(p[0]-p[1])>epsilon:
				return False
	for pair in zip(wp,wp_new):
		for p in zip(pair[0],pair[1]):
			if abs(p[0]-p[1])>epsilon:
				return False
	return True



y=[[enkoder(x[alpha],j) for j in range(16)] for alpha in range(3)]
xp=[[dekoder(y[alpha],k) for k in range(25)] for alpha in range(3)]

def A(p,alpha):
	return (xp[alpha][p]-x[alpha][p])*Df( sum(wp[p][i]*y[alpha][i]+bp[p] for i in range(16)))

def B(p,alpha):
	return sum( (xp[alpha][k]-x[alpha][k])*Df(sum(wp[k][i]*y[alpha][i]+bp[k] for i in range(16)))*wp[k][p]*Df(sum(w[p][j]*x[alpha][j]+b[p] for j in range(25)))  for k in range(25))

wp_new=[]
for p in range(25):
	wp_new.append([])
	for q in range(16):
		wp_new[p].append(wp[p][q]-c*(sum( A(p,alpha)*y[alpha][q] for alpha in range(3) )) )

bp_new=[]
for p in range(25):
	bp_new.append(bp[p]-c*(sum(A(p,alpha) for alpha in range(3))))

w_new=[]
for p in range(16):
	w_new.append([])
	for q in range(25):
		w_new[p].append(w[p][q]-c*(sum( B(p,alpha)*x[alpha][q] for alpha in range(3)) ))

b_new=[]
for p in range(16):
	b_new.append(b[p]-sum(B(p,alpha) for alpha in range(3)) )

m=(max([xp[alpha][k]-x[alpha][k] for k in range(25) for alpha in range(3)])**2)/2.0
while m>epsilon:
	print(m)
	wp=wp_new
	bp=bp_new
	w=w_new
	b=b_new

	y=[[enkoder(x[alpha],j) for j in range(16)] for alpha in range(3)]
	xp=[[dekoder(y[alpha],k) for k in range(25)] for alpha in range(3)]

	for p in range(25):
		bp_new[p]=bp[p]-sum(A(p,alpha) for alpha in range(3))
		for q in range(16):
			wp_new[p][q]=(wp[p][q]-c*sum( A(p,alpha)*y[alpha][q] for alpha in range(3) ))
	for p in range(16):
		b_new[p]=b[p]-sum(B(p,alpha) for alpha in range(3)) 
		for q in range(25):
			w_new[p][q]=w[p][q]-c*(sum(B(p,alpha)*x[alpha][q]  for alpha in range(3) ))
	m=(max([xp[alpha][k]-x[alpha][k] for k in range(25) for alpha in range(3)])**2)/2.0




def f_1(x):
	return 1 if x>=0 else 0
	
for alpha in range(3):
	mod=1
	for k in range(25):
		print(f_1(sum(wp[k][i]*y[alpha][i]+bp[k] for i in range(16))), end='')
		if mod%5==0:
			print('')
		mod+=1
	print('')

