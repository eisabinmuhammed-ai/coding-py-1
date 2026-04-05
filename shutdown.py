user=input("do you want to shut down: ")
def shutdown(user):
    if user=="yes":
        return "shutdown"
    elif user=="no":
        return "abort shutdown"
    else:
        return "sorry"
print(shutdown(user)) 