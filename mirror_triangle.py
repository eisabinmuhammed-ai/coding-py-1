print("hafe piremed patern of (*) ")
n=int(input("enter number of rows"))
for i in range(n):
    for J in range(i+1):
        if (J<=n-i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()