class Solution(object):
    def isPalindrome(self, s):
        s1=''.join (ch.lower() for ch in s if ch.isalnum())
        return s1==s1[::-1]
       


       