def add(q,p):
    return q+p
def subtract(q,p):
    return q-p
def multiply(q,p):
    return q*p
def dived(q,p):
    return q/p
choci=input("enter if you want to add,subtract,muliply or dived: ")
sum1=int(input("enter numer you want to: "))
sum2=int(input("enter a another number to put: "))
if choci == "add":
    print(sum1,"+",sum2,"=",add(sum1,sum2))
elif  choci == "subtract":
    print(sum1,"-",sum2,"=",subtract(sum1,sum2))
elif choci == "multiply":
    print(sum1,"*",sum2,"=",multiply(sum1,sum2))
elif choci == "dived":
    print(sum1,"/",sum2,"=",dived(sum1,sum2))
else:
    print("invalid choce")