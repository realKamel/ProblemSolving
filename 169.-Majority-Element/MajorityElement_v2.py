from typing import Counter, List

class Solution:
    # Time Complexity O(n)
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]
     
x = Solution().majorityElement([3,2,3])