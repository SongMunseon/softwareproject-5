def factorial(n):
    sum=1
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            sum*=i
        return sum


def Cf(d,f):
    if d==f:
        return 1
    else:
        try:
            return factorial(d)/(factorial(f)*factorial(d-f))
        except:
            print("error")

def C(x,y):
    if x==y or y==0:
        return 1
    else:
        return C(x-1,y) + C(x-1,y-1)


a = int(input("a 입력 : "))
b = int(input("b 입력 : "))

print(Cf(a,b))
print(factorial(5))
print(C(a,b))