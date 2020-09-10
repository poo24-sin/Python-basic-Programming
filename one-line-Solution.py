#factorial

def factorial(n):
    return 1 if(n == 1 or n==0) else n * factorial(n-1)

num = int(input("Enter any digit to find factorial"))
print("The Factorial of ",num," is : ",factorial(num))