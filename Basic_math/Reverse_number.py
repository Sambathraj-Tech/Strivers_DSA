def reverse_number(n):
    
    result = 0
    
    while n > 0:
        
        last_digit = n % 10 # extract the lastdigit
        result = (result * 10) + last_digit # add the extracted digit
        n = n // 10 # remove the last digit for the next loop
    
    print(result)
    
n = int(input("Enter the number to be reversed: "))
reverse_number(n)
        