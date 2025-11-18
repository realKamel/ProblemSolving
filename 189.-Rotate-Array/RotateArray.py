from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        listLenght = len(nums)
        k = k % listLenght  # Handle cases where k > listLenght
        nums[:] = nums[listLenght - k:] + nums[:listLenght - k]


result = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)

print(result)
