#!/usr/bin/env python3
#Neuron McCullocha-Pittsa
def f(u):
	return 0 if u<0 else 1
def y(w,u):
	return f(sum(w[i]*u[i] for i in range(len(w))))

#bramki logiczne
NOT=[-1,0]
gates={
	"AND":[0.5,0.5,-1],
	"NAND":[-0.6,-0.6,1],
	"OR":[1,1,-1],
}
notValues=[(0,1),(1,1)]
triValues=[(i,j,1) for i in range(2) for j in range(2)]

print("NOT")
for wi in notValues:
	print(wi,y(wi,NOT))

for t in ["AND","NAND","OR"]:
	print(t)
	for wi in triValues:
		print(wi,y(wi,gates[t]))
