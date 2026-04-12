import random
while True:
    user_chois=input("put rock,paper,sissers:  ")
    possibel=["rock","sissers","paper"]
    comper_chois=random.choice(possibel)
    print(f"you put {user_chois} and computer puts {comper_chois}")
    if comper_chois == user_chois:
        print("its a tie")
    elif comper_chois =="rock":
        if user_chois=="paper":
            print("paper covers rock")
        else:
            print("rock breaks sissers")
    elif comper_chois =="sissers":
        if user_chois=="paper":
            print("paper is cut by sissers")
        else:
            print("rock breaks sissers")
    elif comper_chois =="paper":
        if user_chois=="rock":
            print("paper covers rock")
        else:
            print("rock breaks sissers")
    done=input("do you want to play again (y/n): ")
    if done  == "n":
        break