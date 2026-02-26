user_input = input("Enter a single character: ")

# We check length to ensure the user didn't enter a whole word
if len(user_input) == 1:
    if user_input.isdigit():
        print(f"Yes, '{user_input}' is a number.")
    else:
        print(f"No, '{user_input}' is not a number.")
else:
    print("Please enter only one character.")