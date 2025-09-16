def f(arr, i):            # ([1,2,3,4,5]
    n = len(arr)          # 5
    if i >= n//2:         # 0 > 2
        return
    arr[i] ,arr[n - i -1] = arr[n - i -1], arr[i]  # swap ->0, 4 = 4 , 0
    return f(arr, i+1)    # f([5,2,3,4,1] ,0+1 = 1)
arr = [1, 2 ,3, 4, 5]
print("Original Array :", arr)
f(arr, 0)
print("Reversed Array :", arr)
