def f(n):
    if n == 0:
        return 1
    return n * f(n-1)
        
n = int(input("Enter a number: "))# 5
print(f(n))

Output:
Enter a number: 5
120
