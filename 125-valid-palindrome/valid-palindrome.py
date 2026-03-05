class Solution(object):
    def isPalindrome(self, s):
        s1=''.join (ch.lower() for ch in s if ch.isalnum())
        left,right=0,len(s1)-1
        while left<right:
            if s1[left]!=s1[right]:
                return False
            left+=1
            right-=1

      
        return True       


       