rowsize=int(input("enter row size:  "))
if rowsize%2==0:
    hafedimrow=int(rowsize/2)
else:
    hafedimrow=int(rowsize/2)+1
space=hafedimrow-1
for i in range (1,hafedimrow+1):
    for j in range (1,space+1):
        print(end=" ")
    num=1
    space=space-1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,hafedimrow):
    for j in range(1,space+1):
        print(end=' ')
    space=space=+1
    num=1
    for j in range(1,2*(hafedimrow-i)):
        print(end=str(num))
        num=num+1
    print()         