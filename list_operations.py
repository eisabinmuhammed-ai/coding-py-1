l=[3,8,4,9,6,1]
print("te origenel list is ",l)
sum=0
for i in l:
    sum=sum+i
avg=sum/len(l)
print("sum=",sum)
print(avg)
l.sort()
print("the smallest element is ",l[0])
print("large element is ",l[-1])
