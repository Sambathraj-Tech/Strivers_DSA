def f(n):
	   if n == 0:
	      return 0
	   return n + f(n-1)
	    
	n = int(input("Enter a number: "))# 3
	print(f(n))

Output:
Enter a number: 3
6
