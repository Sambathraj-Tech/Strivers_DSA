SOLUTION -1 :
class Solution(object):
    def reverse(self, x):
        is_negative = False     # assume it false for lastly change into negative
        if x < 0:
            is_negative = True  # Says true to execute next line
            x *= -1             # convert negative into positive
        res = 0
        while x > 0:            # From this line every x value is only positive
            res = (res * 10) + (x % 10)
            x = x // 10
        if res > 2 ** 31 -1:    # As per the question check the range 
            return 0
        if is_negative:         # When the input is negative then is_negative is change into True 
                                  so we check is_negative is True then res * -1 as per the question
            return res * -1
        else:
        return res
        
SOLUTION - 2: BULIT IN FN:

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res
