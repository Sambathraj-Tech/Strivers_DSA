def armstrong_number(n):
    res = 0
    copy = n
    while n > 0:
        temp = n % 10
        res = res + (temp ** 3)
        n = n // 10
    if res == copy:
        print(f"{res} is a Armstrong Number.")
    else:
        print(f"{res} is not a Armstrong Number.")
armstrong_number(153)
=====================================================================================================================

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
