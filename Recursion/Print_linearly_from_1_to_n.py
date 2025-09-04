def f(i , n):                       # (1, 4)
    if i > n :                      # (1 > 4)
        return
    print(i)                        # 1
    f(i + 1, n)                     # (2, 4)

n = int(input("Enter the number: "))# 4
f(1, n)                             #(1,4)

Output: 
Enter the number: 4
1
2
3
4
