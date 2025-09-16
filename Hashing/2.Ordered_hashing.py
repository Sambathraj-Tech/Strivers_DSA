* In my understanding to uses the dictionary instead of List 
* Becase in list we do [0] * 10 = [0,0,0,0,0,0,0,0,0] .But in Dictionary {1: 2, 2: 2} Its easier no need to multiply just Mapping.
* One more thing is Input also we provided

count = int(input("How many numbers to be counted: ")) # 5
frequency = {}                                         # empty Dict
for i in range(count):                                 # 0, 1, 2, 3, 4
    num = int(input())                                 # 1 ,1, 2, 3, 2
    
    # If the number is already in the dictionary, increase its count
    if num in frequency:
        frequency[num] += 1 
    # If it's not in the dictionary, add it with count 1 
    else:
        frequency[num] = 1
'''           {key    :         value pairs} 
iteration  | input | if in frequency | else |   o/p  |    
   0       |   1   |  no             |   1  | {1 : 1}|
   1       |   1   |  yes : {1 : 2}  |      | {1 : 2}|
   2       |   2   |  no             |   1  | {2 : 1}|
   3       |   3   |  no             |   1  | {3 : 1}|
   4       |   2   |  yes : {2 : 2}  |      | {2 : 2}|
'''   
check = int(input('Enter a to be check: '))            #1 
print(f"{check} is appears {frequency[check]}")        # 1 is appears 2 times

for key in sorted(frequency):    # Sorted op
  print(key, frequency[key])
