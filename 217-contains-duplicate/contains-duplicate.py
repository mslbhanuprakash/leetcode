class Solution(object):
    def containsDuplicate(self, nums):
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            if freq[i]>1:
                return True
       
        return False
        