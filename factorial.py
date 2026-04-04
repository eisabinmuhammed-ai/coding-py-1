def factorial(x):
    """the factorial is"""
    if x==0 or x==1:
        return 1
    else:
       return x*factorial(x-1)
num=int(input("enter number: "))
print(factorial.__doc__)
print("factorial of ",num,"is ",factorial(num))