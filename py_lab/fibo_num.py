#!/usr/bin/python3

F=[]
F.insert(0,1)
F.insert(1,1)
n=int(input("how much n: "))
for i in range(2,n):
	F.append(F[i-1]+F[i-2])
for i in range(0,n):
	print("%d " % F[i])
print('F%d = %d ' % (n, F[n-1]))
