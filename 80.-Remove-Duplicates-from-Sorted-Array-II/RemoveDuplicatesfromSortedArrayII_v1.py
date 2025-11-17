from typing import Dict,List


class Solution:
    # Time Complexity O(n^2)
    def removeDuplicates(self, nums: List[int]) -> int:
        enties_count: Dict[int, int] = dict()
        end = len(nums)
        k = end
        for i in range(end):
            if (enties_count.get(nums[i], 0) != 0):
                enties_count[nums[i]] = enties_count[nums[i]] + 1
            else:
                enties_count[nums[i]] = 1

        for idx in range(end):
            while enties_count[nums[idx]] > 2:
                for temp in range(idx+1, end):
                    nums[temp-1] = nums[temp]
                k = k-1
                enties_count[nums[idx]] = enties_count[nums[idx]] - 1

        return k
