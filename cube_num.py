def cube(num):
    return num*num*num
def by_three(num):
    if num %3 ==0:
        return cube(num)
    else:
        return False
enter=int(input("enter number: "))
print(by_three(enter))