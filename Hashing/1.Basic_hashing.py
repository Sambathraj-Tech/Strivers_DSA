 def f(arr, n):
    count = 0
    for i in range(0, len(arr)):
        if arr[i]  == n:
            count += 1
    return count
arr = [1, 2, 3, 1, 2]
n = int(input("Enter a number: "))
print(f(arr, n))

Output:
Enter a number: 19
0
Enter a number: 2
2

Time Complexity : O(n) Because it iterates every number in the array.
