class Solution(object):
    def countEven(self, num):
        count=0
        for x in range(1,num+1):
            s=sum(map(int,str(x)))
            if s%2==0:
                count+=1
        return count
                     
        