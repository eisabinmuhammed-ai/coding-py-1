import array as arr
array_num=arr.array('i',[1,2,3,4,5,4,7,4])
print("number of times 4 appers :",str(array_num.count(4)))
array_num.reverse()
print("revers the order of times")
print(str(array_num))