#lEET CODE 26

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 1
        for i in range(0,len(nums)):
            if(len(nums)!=i+1 and nums[i]<=nums[i+1]):
                if(nums[i]==nums[i+1]):
                    i = i+1
                else:
                    nums[last] = nums[i+1]
                    last = last+1
            else:
                break   
        return last

                        