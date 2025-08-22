def armstrong_number(n):
    check = n
    num_digits = len(str(n)) # int > 1634 > str "1634" > len(4)
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum = sum + pow(last_digit, num_digits)# 3 or 4
        n = n // 10
        
    if check == sum:
        print(f"{check} is a armstrong number")
    else:
        print(f"{check} is not a armstrong number")
n = int(input("Enter the armstrong number: "))
armstrong_number(n)
