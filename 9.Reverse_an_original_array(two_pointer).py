def f(arr, l , r): (0, 4)
    if l >= r:                       # 0 >= 4 
        return
    arr[l] , arr[r] = arr[r], arr[l] # 5, 2, 3, 4, 1
    f(arr, l+1, r-1)                 # ([5, 2, 3, 4, 1], 1, 3)
    
arr = [1, 2, 3, 4, 5]
print("Original Array :", arr)
f(arr, 0, len(arr) - 1)              # (arr = [1,2,3,4,5], l = 0, r = 4)
print("Reversed Array :", arr)
