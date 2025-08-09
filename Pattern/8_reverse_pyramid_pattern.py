n = 5

for i in range (0,n):
    
    for j in range (0,i,1): # 0,1,2,3,4,5
        print(" ",end = "")
    
    for k in range (0,n-i): # 5,4,3,2,1,0
        print("* ",end= "")    
      
    print()