def f(i, n):                        # f(1 = 3, n = 3)
    if (i < 1):                     # 3 < 1
        return
    print(i)                        # 3
    f(i - 1, n)                     # (3-1=2 , 3)

n = int(input("Enter a number: "))  # input = 3  
f(n, n)                             # f(3,3)

Output:
Enter a number: 3
3
2
1
