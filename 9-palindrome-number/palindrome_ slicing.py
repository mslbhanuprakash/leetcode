class Solution(object):
    def isPalindrome(self, x):
        res=str(x)
        return res == res[::-1]
        
