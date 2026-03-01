mediel_candision=input("do you have any illness,y or n:  ")
if mediel_candision=="y":
    print("you are allowed")
else:
    attendens=int(input("what is your attende: "))
    if attendens>=75:
        print("you are allowed")
    else:
        print("you are not allowed")