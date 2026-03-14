string=input("enter word:  ")
char=input("Enter letter: ")
i=0
cout=0
while i < len(string):
    if string[i]==char:
        cout=cout+1
    i=i+1
print("the letter ",char, " has been repeted",cout,"in the word",string)