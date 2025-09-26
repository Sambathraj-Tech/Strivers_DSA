Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Examples:

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

Brute-Force approach(Using two loops): 

def f(arr, n):
    max_frequency = 0
    min_frequency = n  # 5
    max_element = None
    min_element = None
    visited = [False] * n
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        if count > max_frequency:
            max_element = arr[i]
            max_frequency = count
        if count < min_frequency:
            min_element = arr[i]
            min_frequency = count
    print(f"The maximum element is {max_element} and the frequency is {max_frequency}")
    print(f"The maximum element is {min_element} and the frequency is {min_frequency}")
if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    f(arr, n)
================================================================================================================
Optimized approach(Using map):

def f(arr, n):
    map = {}
    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]]  = 1
            
    max_frequency = 0
    min_frequency = n
    max_element = None
    min_element = None

    for element , count in map.items():
        if count > max_frequency:
            max_element = element
            max_frequency = count
        
        if count < min_frequency:
            min_element = element
            min_frequency = count
    print(f"The max_ele is {max_element} & freq is {max_frequency}")
    print(f"The min_ele is {min_element} & freq is {min_frequency}")
if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    f(arr, n)


