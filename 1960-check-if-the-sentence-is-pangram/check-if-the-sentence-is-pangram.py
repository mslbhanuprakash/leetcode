class Solution(object):
    def checkIfPangram(self, sentence):
        
        alph="abcdefghijklmnopqrstuvwxyz"
        for i in alph:
            if i not in sentence:
                return False
            
        return True
    
   
        