Palindrome of a String:

def f(i, palindrome):                           # i=0, madam
    n = len(palindrome)                         # 5
    if i > n//2:                                # 0 > 2
        return True
    if palindrome[i] != palindrome[n - i - 1]:  # 'm' != 'm'
        return False
    return f(i + 1, palindrome)                 # f(i=1, madam)
     
palindrome = "madam"                            
print(f(0, palindrome))                          # 0, madam

Output: 
True




125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


class Solution(object):
    def isPalindrome(self ,s) :
        s = ''.join(c.lower() for c in s if c.isalnum()) # 1st -> for c in c.isalnum, 2nd->lower(), 3rd-> join()
        left = 0
        right = len(s) - 1                               # -1 why? Becoz len()-> counts start from 1 ,but in python index starts from 0
        while left < right :                             # 0 < len(right) -1 
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

Time Complexity =  check half(left < right) -> O(n/2) 
Space Complexity = Auxillary space left = 0,right = len(s) - 1 
