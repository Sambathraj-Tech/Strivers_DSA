def f(i, n):                       # (1, 3)
    if i > n:                      # (1 > 3)
        return
    f(i + 1, n)                    # (1+1=2 ,3)
    print(i)
n = int(input("Enter a number: ")) # 3
f(1, n)                            # (1, 3)

Output:
Enter a number: 3
3
2
1
