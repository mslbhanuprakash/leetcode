class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for i in t:
            if i not in freq:
                return False
            freq[i]-=1
            if freq[i]<0:
                return False
        return True     
        

        