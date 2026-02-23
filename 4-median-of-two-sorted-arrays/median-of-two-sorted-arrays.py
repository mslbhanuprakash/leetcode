class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        mer=nums1+nums2
        mer.sort()
        m=len(mer)
        if m%2 ==0:
            first_mid=mer[m//2-1]
            sec_mid=mer[m//2]
            med=float(first_mid+sec_mid)/2

        else:
            med=mer[m//2]
        return med    

        