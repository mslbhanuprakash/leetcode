class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq={}
        for ch in magazine:
            if ch not in freq:
                freq[ch]=0
            freq[ch]+=1
        for ch in ransomNote:
            if ch not in freq or freq[ch]==0:
                return False
                break
            freq[ch]-=1
        else:
            return True        