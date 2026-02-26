def ascii_checker():
    user_input = input("Enter a single character: ")

    # Validation: ord() only accepts a string of length 1
    if len(user_input) == 1:
        value = ord(user_input)
        print(f"The ASCII/Unicode value of '{user_input}' is: {value}")
    else:
        print("Error: Please enter exactly one character.")

if __name__ == "__main__":
    ascii_checker()