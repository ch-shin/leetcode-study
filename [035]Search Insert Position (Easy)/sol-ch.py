class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            return binary_search(nums, 0, len(nums) - 1, target)


def binary_search(nums, low, high, target):
    while low <= high:
        mid = (high + low) // 2
        if (nums[mid] == target):
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low