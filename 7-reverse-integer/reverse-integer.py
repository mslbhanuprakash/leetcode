class Solution(object):
    def reverse(self, x):
        sign= -1 if x<0 else 1
        x=abs(x)
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev<-2147483648 or rev>2147483648:
            return 0

        return sign*rev 
        
        
            
