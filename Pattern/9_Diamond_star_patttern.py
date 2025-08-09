def pattern(n):
    for i in range (0,n):
        
        for j in range (0,n-i-1):
            print(" ", end="")
        for k in range (0,i+1):
            print("* ", end="")
            
        print()
    for i in range(0,n):
        
        for j in range (0,i,1):
            print(" ",end= "")
        for k in range (0,n-i):
            print("* ",end= "")
            
        print()

a = pattern(5)