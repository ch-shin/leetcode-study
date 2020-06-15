class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = pivot_binary_search(nums)

        if pivot <= 0:
            return target_binary_search(nums, 0, len(nums) - 1, target)

        if target >= nums[0]:
            return target_binary_search(nums, 0, pivot, target)
        else:
            return target_binary_search(nums, pivot, len(nums) - 1, target)


def pivot_binary_search(nums):
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mid = (high + low) // 2
        if nums[mid - 1] > nums[mid]:
            return mid
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def target_binary_search(nums, low, high, target):
    while (low <= high):
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = (mid + 1)
        else:
            high = (mid - 1)
    return -1
