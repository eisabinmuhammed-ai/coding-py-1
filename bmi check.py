w=int(input("what is your wight: "))
h=int(input("what is your hight: "))
bmi=w/ (h/100)**2
if bmi<= 18.4:
    print("you are underwight")
elif bmi <=24.9:
    print("you are healty")
elif bmi <=29.9:
    print("you are over weight")
elif bmi <=34.9:
    print("you are very over weight")
elif bmi <=39.9:
    print("you are obese")
else:
    print("you are very obese") 
