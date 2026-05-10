num1=[1,2,3]
num2=[4,5,6]
result=map(lambda y,x:y+x,num1,num2)
print("addsion of two lists are ")
print(list(result))

num=[1,2,3]
def sq(n):
    return n*n
square=list(map(sq,num))
print(square)