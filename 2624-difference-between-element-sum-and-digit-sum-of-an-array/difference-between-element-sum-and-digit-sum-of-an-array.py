class Solution(object):
    def differenceOfSum(self, nums):
        res1=sum(nums)
        res2=[]
        for i in nums:
            res2+=list(str(i))
        res2=[int(x) for x in res2]
        res3=sum(res2)
        return abs(res1-res3)


       