from math import gcd
from math import sqrt,ceil
from random import randint

def mod_rel(a,N):
	r=2
	while (a**r)<N*N:
		if ((a**r)-1)%N==0:
			return r
		r+=1
	return 0
def factorize(N):
	check=True
	while check:
		r=0
		while r==0:
			a=randint(1,N)
			r=mod_rel(a,N)
		x=gcd(N,int(a**(r/2))+1)
		if x>1:
			check=False
			print(x)
		x=gcd(N,int(a**(r/2))-1)
		if x>1:
			check=False
			print(x)
		
factorize(13843)
factorize(988027)
