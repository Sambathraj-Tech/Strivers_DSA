def f(i, n): #1, 4
    if i > n:  1 > 4
        return
    
    print("Sambath")
    f(i+1, n) # 2, 4

n = int(input("Enter a number: ")) #4
f(1 ,n) # (1,4)

TIME COMPLEXITY : BIG O(N), SPACE COMPLEXITY : BIG O(N)
