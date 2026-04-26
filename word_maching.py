def mach_word(words):
    crt=0
    a=[ ]
    for word in words:
        if len(words) > 1 and word[0]==word[-1]:
            crt=crt+1
            a.append(word)
    print(a)
    return crt
count=mach_word(["qeq","qas","eut","cvb"])
print("number of word haveing first and last charecter same ",count)