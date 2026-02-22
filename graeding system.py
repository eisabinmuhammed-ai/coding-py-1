print("enter marks of 5 subjekts : ")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
totel=mark1+mark2+mark3+mark4+mark5
avr=(totel/5)
if (avr>=91)and avr<100:
    print("A1")
elif avr>=81 and avr<91:
    print("A2") 
elif avr>=71 and avr<81:
    print("b1")
elif avr>=61 and avr<71:
    print("b2")
elif avr>=51 and avr<61:
    print("c1")
elif avr>=41 and avr<51:
    print("c2")
elif avr>=31 and avr<41:
    print("d")
elif avr>=0 and avr<31:
    print("e")
else:
    print("invaled input ")    