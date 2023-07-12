#LEETCODE 27

class Solution:
    def removeElement(self,nums, val) -> int:
        last = 0
        for i in range(0,len(nums)):
            j = i+1
            if(nums[i] == val):
                while(len(nums)!=j):
                    if(nums[j]!=nums[i]):
                        nums[i] = nums[j]
                        nums[j] = val
                        last = i+1
                        break
                    else:
                        j = j+1
            else:
                last = i+1
        print(nums)
        return last


print(Solution().removeElement([3,2,2,3],3))