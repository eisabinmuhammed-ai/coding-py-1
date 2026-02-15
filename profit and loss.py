ac=int(input("enter price of money use to buy stuff  : "))
sp=int(input("enter price of money use to sale stuff  : "))
if (sp>ac):
    amount= sp - ac
    print("totel Profit is {0}".format(amount))
else:
    print("no profit!!!")