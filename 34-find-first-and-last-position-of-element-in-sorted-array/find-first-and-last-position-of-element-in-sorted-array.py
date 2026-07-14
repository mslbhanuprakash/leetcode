class Solution(object):
    def searchRange(self, nums, target):
        indexes=[]
        for i in range(len(nums)):
            if nums[i]==target:
                indexes.append(i)
        if indexes:
            
            return [indexes[0], indexes[-1]]

        return [-1, -1]

    