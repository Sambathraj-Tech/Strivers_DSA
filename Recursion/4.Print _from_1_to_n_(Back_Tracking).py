def f(i, n):                       #(3,3)
    if i < 1:                      #3<1
        return
    f(i - 1, n)                    #(3-1=2, 3)
    print(i)
    
n = int(input("Enter a number: ")) #3
f(n,n)                             #(3,3)
 
Output:
Enter a number: 3
1
2
3   
