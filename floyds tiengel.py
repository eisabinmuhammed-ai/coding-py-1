rows=int(input("enter numbers of rows:  "))
num=1
for i in range (1,rows+1):
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print() 