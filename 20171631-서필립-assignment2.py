n = int(input("Enter a number : "))
f = 1

while n>=0:
    for i in range(1,n+1) :
        f *= i
    print(n,"! =", f)
    f = 1
    n = int(input("Enter a number : "))

    if n < -1 :
        print("Can't execute")
        for i in range(1,n+1) :
            f *= 1
        f = 1
        n = int(input("Enter a number : "))
    elif n == -1 :
        break
