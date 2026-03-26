class Solution(object):
    def firstPalindrome(self, words):
        res=""
        for word in words:
            if word[::-1]==word:
                res=res+word
                break
            else:
                res
        return res   
        