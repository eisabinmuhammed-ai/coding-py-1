units=int(input("hoe many units didyou consum:  "))
if (units<50):
    amount=units*2.60
    surcharcg=25
elif units>=100:
    amount=130+((units-50)*3.25)
    surcharcg=35
elif units>=200:
    amount=130+162.5+((units-100)*5.26)
    surcharcg=45
else:
    amount=130+162.5+526+((units-200)*8.45)
    surcharcg=75
totel=amount+surcharcg
print("electesty bills =",totel) 