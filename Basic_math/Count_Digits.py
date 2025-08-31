def count_digits(n):
    count = 0
    while n != 0:
        count += 1 # every time the loop executes the count is increased
        n = n // 10  # floor division avoids float values
    print(count)
count_digits(int(input("Enter the numbers to be counted: ")))# 12345


output: 
Enter the numbers to be counted: 12345
5
