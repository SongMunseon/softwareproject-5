num = int(input("숫자를 입력하세요"))
def Factorial(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return Factorial(num-1) * num
print(Factorial(num))



