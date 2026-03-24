class Solution(object):
    def countAsterisks(self, s):
        xor=0
        count=0
        for ch in s:
            if ch=='|':
                xor^=1
            elif ch=='*'and xor==0:
                count+=1
        return count        
        