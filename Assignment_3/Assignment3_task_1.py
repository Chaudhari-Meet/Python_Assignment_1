def Factorial(n):
    fact=1
    if(n==0 or n==1):
        return 1
    else:
        fact = n*Factorial(n-1)
        return fact

num= int(input("Enter the number to find its factorial :"))
print(f"The factorial of {num} is {Factorial(num)}.")