#!/usr/bin/env python3
#Metoda gradientu

from random import uniform
#x=(x_1,...,x_n)
def fmin(f,fderivatives,x,c,epsilon):
	while(1):
		xnew=[x[i]-c*fderivatives[i](x) for i in range(len(x))]
		if max(map(lambda pair:abs(pair[0]-pair[1]), zip(xnew,x))) < epsilon:
			return xnew 
		else:
			x=xnew
#przykłady:
epsilon=0.00000001
c=0.01
def f(x):
	return 2*pow(x[0],2)+2*pow(x[1],2)+pow(x[2],2)-2*x[0]*x[1]-2*x[1]*x[2]-2*x[1]*x[2]-2*x[0]+3
fderivatives=(
	lambda x: 4*x[0]-2*(x[1]+1),
	lambda x: -2*(x[0]-2*x[1]+x[2]),
	lambda x: 2*x[2]-2*x[1]
)

print('c:'+str(c)+'\t'+str(fmin(f,fderivatives,[uniform(-1.0,1) for i in range(3)],c,epsilon)))

def g(x):
	return 3*pow(x[0],4)+4*pow(x[0],3)-12*pow(x[0],2)+12*pow(x[1],2)-24*x[1]
gderivatives=(
	lambda x: 12*x[0]*(pow(x[0],2)+x[0]-2),
	lambda x: 24*(x[1]-1)
)
x=min([fmin(g,gderivatives,x,c,epsilon) for x in [(uniform(-i,i),uniform(-i,i))  for i in range(0,4)]], key=g)
print("c: {}\t{} g({})={}".format(c,x,x,g(x)))
