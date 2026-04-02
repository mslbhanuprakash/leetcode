class Solution(object):
    def sortedSquares(self, nums):
        square=sorted([x**2 for x in nums])
        return square
        