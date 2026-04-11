try:
    num1,num2=eval(input("enter 2 numbers: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("pls dont put zero")
except SyntaxError:
    print("put comma")
except ValueError:
    print("put a number")
finally:
    print("This will execute nomater what")