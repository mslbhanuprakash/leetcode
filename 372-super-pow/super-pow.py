class Solution(object):
    def superPow(self, a, b):
        mod=1337
        res=1
        for digit in b:
            res=(res**10)*(a**digit)
            res=res%mod
        return res
       
        