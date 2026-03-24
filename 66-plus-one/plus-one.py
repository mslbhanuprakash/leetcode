class Solution(object):
    def plusOne(self, digits):
        num=0
        for digit in digits:
            num=num*10+digit
        num+=1
        res=[]
        for n in str(num):
            res.append(int(n))
        return res
   

        