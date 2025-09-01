def print_divisors(divisor: int):
    for i in range(1, divisor+1):
        if divisor % i == 0:          # always put divisor 1st then divided value which is i
            print(i, end=" ")
print_divisors("Enter the Divisor: ")
