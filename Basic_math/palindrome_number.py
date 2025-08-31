	class Solution(object):
	    def is_Palindrome(self, x):
	        if x < 0:                         # x less than 0 or negative int return False
	            return False
	        elif x >= 0:                      # x greater than 0 or equal to 0 then proceed
	            res = 0                       # Insert the reverse numbers in this variable
	            copy = x                      # Take copy before reverse the number 
	            while x > 0:                  
	                temp = x % 10             # Take the last digit of the numbers
	                res  = (res * 10) + temp  # 1st -> * 10 then add the temp (e.g: 5*10 = 50 (50+3 = 53))
	                x    = x // 10            # Remove the last digit from the numbers
            return res == copy                # Compare and return True
