n = int (input("Enter the rows : "))

for i in range (1,n+1):
    for j in range (i):
        print(chr(64+i), end= " ")
    print()