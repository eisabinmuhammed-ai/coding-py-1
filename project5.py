def power_with_loop(base, exponent):
    result = 1
    for _ in range(int(exponent)):
        result *= base
        
    return result

n = float(input("Enter the base (n): "))
p = int(input("Enter the power (integer): "))

final_value = power_with_loop(n, p)
print(f"{n} raised to the power of {p} is: {final_value}")