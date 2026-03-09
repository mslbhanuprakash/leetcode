class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        right=len(nums)-1
        left=0
        p1=nums[right]*nums[right-1]*nums[right-2]
        p2=nums[left]*nums[left+1]*nums[right]
        return max(p1,p2)
        
        
        