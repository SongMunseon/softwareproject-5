import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
	a = 0
	b = 1
	if n <= 1:
		return n
	for i in range(n):
		return a
		a = b
		b = a + b  


while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

