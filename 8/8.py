#!/usr/bin/env python3
import random
from math import exp

class Interface:
	def __init__(self,v):
		if isinstance(v,list) and len(v)>0:
			self.v=v
		else:
			self.v=[(0 if x==' ' else 1) for x in v.replace('\n','')]
	def __str__(self):
		return '\n'.join([''.join([('*' if x==0 else ' ') for x in row]) for row in ((self.v[i*5:(i+1)*5]) for i in range(5))])
	def __getitem__(self,arg):
		return self.v[arg]
	def __len__(self):
		return len(self.v)
	def get_value(self):
		if self.v == [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]:
			return 1
		if self.v == list([0 if x == 1 else 1 for x in z]):
			return 2
		return 0
	def __bool__(self):
		z=[0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]
		return self.v == z or self.v == list([0 if x == 1 else 1 for x in z])
z=Interface([0,0,0,0,0,
0,1,1,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0])

random.seed()

xs=[random.randint(0,1) for i in range(25)]
c=[[ (z[i]-0.5)*(z[j]-0.5) if i!=j else 0 for j in range(25) ] for i in range(25)]
w=[[2*c[i][j] for j in range(25)] for i in range(25)]
theta=[sum(c[i][j] for j in range(25)) for i in range(25)]

for T in [2.8]:
	print("#################")
	print("Temperatura: {}".format(T))
	def f(u):
		return 1/(1+exp(-u/T))


	def dynamics(x):
		u=[sum(w[i][j]*x[j] for j in range(25))-theta[i] for i in range(25)]
		x=[(1 if random.uniform(0,1)<=f(u[i]) else 0) for i in range(25)]
		return x
	x=xs

	
	print(Interface(x))
	print("\n")
	
	checks=[False,True,True]
	
	for t in range(10000):
		x=dynamics(x)
		inter=Interface(x)
		if(checks[inter.get_value()]):
			checks[inter.get_value()]=False
			print("Iteration: {}".format(t))
			print(inter)
			print("\n")
