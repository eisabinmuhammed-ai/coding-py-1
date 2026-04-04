def tip(amownt,tip_persent):
    totel=amownt*(1+0.01*tip_persent)
    totel=round(totel,2)
    print(f"totel is ${totel}")
num1=int(input("enter amount: "))
num2=int(input("enter tip: "))
print(tip(num1,num2))