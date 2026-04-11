vaild=False
while not vaild:
    try:
        n=int(input("Enter number: "))
        while n%2==0:
            print("bye")
        vaild=True
    except ValueError:
        print("invaild")
