
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))


even_squares = []
odd_squares = []


for num in range(start_num, end_num + 1):
    square = num ** 2  
    
   
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)


print(f"\nResults for the range {start_num} to {end_num}:")
print(f"Even Squares: {even_squares}")
print(f"Odd Squares:  {odd_squares}")
