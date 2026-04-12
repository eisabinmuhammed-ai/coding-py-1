try:
    age=int(input("enter age: "))
    if age%2==0:
        result="even"
    else:
        result="odd"
    print("it is ",result)  
except ValueError:
    print("You have to enter number")
