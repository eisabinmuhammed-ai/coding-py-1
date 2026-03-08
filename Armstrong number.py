num=int(input("enter number:  "))
sum=0
temp=num
while temp>0:
    dighit=temp%10
    sum+=dighit ** 3
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")