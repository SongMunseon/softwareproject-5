import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)
def iterfibo(n):
	a = 1
	b = 1
	c = 0

	if n <=1:
		return n
	elif n == 2:
		return 1
	else:
		for i in range (n-2):
			c = a + b
			a = b
			b = c

		return c





while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))


