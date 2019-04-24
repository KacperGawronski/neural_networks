#!/usr/bin/env python3
import random

class Interface:
	def __init__(self,v):
		if isinstance(v,list) and len(v)>0:
			self.v=v
		else:
			self.v=[(-1 if x==' ' else 1) for x in v.replace('\n','')]
	def __str__(self):
		return '\n'.join([''.join([('*' if x==0 else ' ') for x in row]) for row in ((self.v[i*5:(i+1)*5]) for i in range(5))])
	def __getitem__(self,arg):
		return self.v[arg]
	def __len__(self):
		return len(self.v)
		
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



def dynamics(x):
	u=[sum(w[i][j]*x[j] for j in range(25))-theta[i] for i in range(25)]
	x=[(1 if u[i]>0 else (0 if u[i]<0 else x[i])) for i in range(25)]
	return x
x=xs
print(Interface(x))
for t in range(5):
	x=dynamics(x)
	print(Interface(x))
