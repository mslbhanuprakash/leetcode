class Solution(object):
    def thirdMax(self, nums):
        res=[]
        for n in nums:
            if n not in res:
                res.append(n)
        if len(res)<3:
            return max(res)
        else:
            res.remove(max(res))
            res.remove(max(res))
        return max(res)    
      

        