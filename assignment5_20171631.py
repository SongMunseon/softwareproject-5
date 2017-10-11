import time

def fibo(n) :
	if n<= 1 :
		return n
	return fibo(n-1) + fibo(n-2)

def iterfibo(n) :
	f0 = 0
	f1 = 1
	iterfibo = 0
	if 0<=n<=1:
		return n
	elif n>1 :
		for i in range(2, n+1) :
			iterfibo = f0 + f1
			f0 = f1
			f1 = iterfibo			
	return iterfibo

while True :
	nbr = int(input("Enter a number: "))
	if nbr<0 :
		break
	ts = time.time()
	iterfibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr,iterfibonumber,ts))
	
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr,fibonumber,ts))
