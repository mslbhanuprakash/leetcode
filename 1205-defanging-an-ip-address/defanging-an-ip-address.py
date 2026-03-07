class Solution(object):
    def defangIPaddr(self, address):
        ad=address.replace(".","[.]")
        return ad