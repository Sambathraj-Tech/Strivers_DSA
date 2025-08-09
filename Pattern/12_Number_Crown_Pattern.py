n = 5
a = 2 * (n-1)

for i in range (1,n+1):
    for j in range (i):
        print(i, end= "")
    
    for k in range (1,a):
        print(" ", end = "")     
        
    for l in range (i,0,-1):
        print(i, end = "")
    a = a - 2
    print()