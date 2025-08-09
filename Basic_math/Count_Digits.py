def count_digits(n):# 12345
    
    count = 0
    
    while n > 0:
        
        last_digit = n % 10 #12345 % 10 = 5  in this pgm this line is not used but i wrote for understanding
        n = n // 10 #12345 // 10 = 1234
        count = count + 1
    print(count)
    
n = int(input("Enter the digits to be counted: "))
count_digits(n)