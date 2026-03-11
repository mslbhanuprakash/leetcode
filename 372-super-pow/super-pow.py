class Solution(object):
    def superPow(self, a, b):
        mod=1337
        res=1
        for digit in b:
            res=pow(res,10,mod)*pow(a,digit,mod)%mod
        return res
       
        