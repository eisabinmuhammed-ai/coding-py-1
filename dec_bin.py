
#convert 5 decimal numbers to binary

for i in range(0,5):
    num=int(input("enter number:  "))
    result = ""
    if num != 0:
        while  num > 0:
            result=str(num%2) + result
            num=(num//2)
        print(result)
    else:
        print(0)