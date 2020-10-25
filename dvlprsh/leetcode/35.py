class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) -1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx) // 2
            mid = nums[mid_idx]
            if mid < target:
                start_idx = mid_idx + 1
            elif mid > target:
                end_idx = mid_idx -1

        return start_idx