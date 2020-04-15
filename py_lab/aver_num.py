#!/usr/bin/python3

n=int(input("how many n:"))
a=list()
b=0
for i in range(n):
	a.append(float(input("number: ")))
	b += a[i]  
c=b / n
print("average is %f" % c)

