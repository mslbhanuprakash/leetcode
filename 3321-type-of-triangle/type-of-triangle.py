class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        side1,side2,side3=nums
        if side1+side2<=side3:
            return "none"
        if side1==side2==side3:
            return "equilateral"
        elif side1==side2 or side2==side3:
            return "isosceles"
        else:
            return "scalene"

        
           
      