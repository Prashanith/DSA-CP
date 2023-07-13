class Solution:
    def findMedianSortedArrays(self, nums1,nums2) -> float:
        l = nums1+nums2
        l.sort()
        ll = int(len(l)/2)
        if(len(l)%2==0):
            return (l[ll]+l[ll-1])/2
        else:
            return l[int(len(l)/2)]

print(Solution().findMedianSortedArrays([1,2],[3,4]))