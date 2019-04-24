#!/usr/bin/env python3
#Perceptron

import numpy as np
import matplotlib.pyplot as plt

#dane wejściowe
u=[
	[0,0,0,0,0,
	0,1,1,0,0,
	0,0,1,0,0,
	0,0,1,0,0,
	0,0,1,0,0,1],
	[0,0,1,1,0,
	0,0,0,1,0,
	0,0,0,1,0,
	0,0,0,0,0,
	0,0,0,0,0,0],
	[0,0,0,0,0,
	1,1,0,0,0,
	0,1,0,0,0,
	0,1,0,0,0,
	0,1,0,0,0,1],
	[0,0,0,0,0,
	0,1,1,1,0,
	0,1,0,1,0,
	0,1,1,1,0,
	0,0,0,0,0,1],
	[0,0,0,0,0,
	0,0,0,0,0,
	1,1,1,0,0,
	1,0,1,0,0,
	1,1,1,0,0,1]
]

w1=[1]*26
def f(u):
	return 0 if u<0 else 1
def scalarMul(w,u):
	return sum(map(lambda x:x[0]*x[1],zip(w,u)))
def sign(t):
	return 1 if t<3 else 0 #3 jest zależne od danych, rozdziela zbiór(listę) na 2 podzbiory
wn=[]
for c in (1.0,0.1,0.01):
	print("c =",c)
	t=counter=0
	w=w1
	while(counter!=4):
		y=f(scalarMul(w,u[t%5]))
		z=sign(t)
		w=[x[0]+c*(z-y)*x[1] for x in zip(w,u[t%5])]
		counter= (counter + 1) if z==y else 0
		t+=1
	print(t)
	for i in range(4):
		print(w[i*5:(i+1)*5])
	print(w[20:])
	wn.append(w)

fig=plt.figure(figsize=(8,8))
for i in range(len(wn)):
	fig.add_subplot(len(wn),1,i+1)
	plt.imshow(-np.array(wn[i][:25]).reshape(5,5), cmap=plt.cm.binary)
plt.show()

