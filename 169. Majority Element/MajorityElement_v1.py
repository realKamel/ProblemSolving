from typing import List


class Solution:
    # Time Complexity O(n)
    def majorityElement(self, nums: List[int]) -> int:
        majorityCount = int(len(nums)/2)
        if(majorityCount < len(nums)/2):
            majorityCount = majorityCount +1
        counter = {}
        for i in range(len(nums)):
            if(counter.get(nums[i],False) == False):
                counter[nums[i]] = 1
            else:
                counter[nums[i]] = counter[nums[i]]+1
        for key,value in counter.items():
            if(value >= majorityCount):
                return key
    
x = Solution().majorityElement([3,2,3])