def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        while(n>1):
            fact *= n
            n -= 1
        return fact

num = 5
print("Factorial of ",num,"is",factorial(num))


def fact(n):
    if n<0:
        return 0;
    elif n==0 or n==1:
        return 1
    else:
        fac = 1
        while n>1:
            fac *= n
            n -= 1
        return fac
num1 = 4
print("factorial",num1,"is",fact(num1))