#!/usr/bin/env python3
#Model asocjacji
import numpy as np
import matplotlib.pyplot as plt

class Interface:
	def __init__(self,v):
		if isinstance(v,list) and len(v)>0:
			self.v=v
		else:
			self.v=[(-1 if x==' ' else 1) for x in v.replace('\n','')]
	def __str__(self):
		return '\n'.join([''.join([('*' if x==1 else ' ') for x in row]) for row in ((self.v[i*5:(i+1)*5]) for i in range(5))])
	def __getitem__(self,arg):
		return self.v[arg]
	def __len__(self):
		return len(self.v)
#dane
ztxt=[]
for i in ["z0.txt","z1.txt"]:
	with open(i,'r') as f:
		ztxt.append(f.read())
z=[Interface(txt) for txt in ztxt]
#macierz W in M_25(Real)
n=25
W=[[(1.0/n)*z[0][i]*z[0][j]+(1.0/n)*z[1][i]*z[1][j] for j in range(len(z[0]))] for i in range(len(z[0]))]

def SGN(X):
	return list(map(lambda x:-1 if x<0 else 1, X))

def F(u):
	return SGN([sum(w[i]*u[i] for i in range(25)) for w in W])

fz0=Interface(F(Interface(ztxt[0])))
fz1=Interface(F(Interface(ztxt[1])))

def printTwoMatrixes(txt1,txt2):
	for row in zip(txt1.split('\n'),txt2.split('\n')):
		print(row[0]+'\t'+row[1])

print("z0\tF(z0)")
printTwoMatrixes(ztxt[0],str(fz0))
print("z1\tF(z1)")
printTwoMatrixes(ztxt[1],str(fz1))

zptxt=[]
for i in ["zp0.txt","zp1.txt"]:
	with open(i,'r') as f:
		zptxt.append(f.read())

fzp0=Interface(F(Interface(zptxt[0])))
fzp1=Interface(F(Interface(zptxt[1])))

print("z'0\tF(z'0)")
printTwoMatrixes(zptxt[0],str(fzp0))
print("z'1\tF(z'1)")
printTwoMatrixes(zptxt[1],str(fzp1))

fig=plt.figure(figsize=(8,8))
fig.add_subplot(3,2,1)
plt.imshow(np.array(fz0[:]).reshape(5,5), cmap=plt.cm.binary)
fig.add_subplot(3,2,2)
plt.imshow(np.array(fz1[:]).reshape(5,5), cmap=plt.cm.binary)

fig.add_subplot(3,2,3)
plt.imshow(np.array(fzp0[:]).reshape(5,5), cmap=plt.cm.binary)
fig.add_subplot(3,2,4)
plt.imshow(np.array(fzp1[:]).reshape(5,5), cmap=plt.cm.binary)

fig.add_subplot(3,2,5)
plt.imshow(np.array(W), cmap=plt.cm.binary)


plt.show()
