class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxi = 0

        while l < r:
            w = r - l
            a = min(height[l], height[r]) * w
            maxi = max(maxi, a)

            if height[l] < height[r]:
                l+= 1
            else:
                r -= 1

        return maxi