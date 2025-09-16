
def f(i , sum):
    if i < 1:
        print(sum)
        return
    f(i-1, sum+i)
    
n = int(input("Enter a number: "))#3
f(n, 0)

Output:
Enter a number: 3
6
