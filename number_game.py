import random
playing=True
turn=1
num=str(random.randint(0,9))
print("this is a number gessing game you have to gess the number between 0 to 9")
while True:
    gess=input("enter number: ")
    if gess == num:
        print("You gesst it in ",turn,"turns")
        playing=False
    else:
        print("\n try one more time")
        turn=turn+1
