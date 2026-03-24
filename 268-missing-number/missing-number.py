class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        res=n*(n+1)//2
        add=sum(nums)
        return res-add

            
        
        