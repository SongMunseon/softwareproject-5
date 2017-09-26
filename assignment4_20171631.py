n = int(input("Enter n:"))
m = int(input("Enter m:"))

def fac(k) :
	answer = 1
	try:
		if k>=0:	
			for i in range(1,k+1):
				answer = answer*i
				i += 1
			return answer
	except:
		print("It can't be executed.`")
val = fac(n)/(fac(m)*fac(n-m))

def Rcs(n,m):
	try:
		if n >=0:	
			if m == 0 or n == m :
				return 1
			else :
                		return Rcs(n-1,m)+Rcs(n-1,m-1)

	except: 
		print("It can't be executed.")
		 
print("Cf(%d,%d):%d" %(n, m, val))
print("C(%d,%d):%d" %(n, m, Rcs(n,m)))
