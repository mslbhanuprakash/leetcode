class Solution(object):
    def majorityElement(self, nums):
        freq={}
        l,r=0,len(nums)-1
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        max_freq=max(freq,key=freq.get)
        return max_freq       
        