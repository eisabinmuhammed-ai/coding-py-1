def paindr(r):
    e=len(r)-1
    s=0
    while(s<e):
        if (r[s]!=r[e]):
            return False
        s=s+1
        e=e-1
    return True
r=(1,2,3,4,5,3,2,1)
if (paindr(r)):
    print("it is a flip flop")
else:
    print("it is not a flip flop")
