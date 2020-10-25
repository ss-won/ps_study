class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            diff = target - v
            if diff in nums[i+1:]:
                return [i, nums.index(diff, i+1)]