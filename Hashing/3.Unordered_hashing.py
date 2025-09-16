* Always Prefer Unordered Mapping.
* We used list & dict . List is used to store large datasets.

n = int(input("How many numbers to be enterd: ")) #5
arr = [] # empty list
for _ in range(n): # 0, 1, 2, 3, 4
    num = int(input()) # 1 ,1, 2, 3, 2
    arr.append(num)    # [1 ,1, 2, 3, 2]
    
frequency = {} # empty dict
for num in arr:  
    # If the number is already in the dictionary, increase its count
    if num in frequency:
        frequency[num] += 1 
    # If it's not in the dictionary, add it with count 1 
    else:
        frequency[num] = 1
'''           key               value pairs
iteration  | input | if in frequency | else |   o/p  |    
   0       |   1   |  no             |   1  | {1 : 1}|
   1       |   1   |  yes : {1 : 2}  |      | {1 : 2}|
   2       |   2   |  no             |   1  | {2 : 1}|
   3       |   3   |  no             |   1  | {3 : 1}|
   4       |   2   |  yes : {2 : 2}  |      | {2 : 2}|
'''   
check = int(input('Enter a to be check: '))   #1 
print(f"{check} is appears {frequency[check]}") # 1 is appears 2 times
