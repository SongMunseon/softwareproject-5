a=0
gap=1
while a>=0:		
	a=int(input("Enter a number: "))
	if a==0:
		print("1")
	elif a<0:
		break 
	else:

		for i in range(1,a+1):
        	        gap*=i
		print(gap)
		gap=1

