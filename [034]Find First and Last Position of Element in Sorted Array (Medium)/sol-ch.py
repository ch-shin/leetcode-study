class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_pivot_idx = binary_search(nums, 0, len(nums) - 1, target)

        # find min
        leftmost_idx = target_pivot_idx
        while True:
            next_left_pivot_idx = binary_search(nums, 0, leftmost_idx - 1,
                                                target)
            if next_left_pivot_idx != -1:
                leftmost_idx = next_left_pivot_idx
            else:
                break

        # find max
        rightmost_idx = target_pivot_idx
        while True:
            next_right_pivot_idx = binary_search(nums,
                                                 rightmost_idx + 1,
                                                 len(nums) - 1,
                                                 target)
            if next_right_pivot_idx != -1:
                rightmost_idx = next_right_pivot_idx
            else:
                break
        return [leftmost_idx, rightmost_idx]


def binary_search(nums, low, high, target):
    while (low <= high):
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = (mid + 1)
        else:
            high = (mid - 1)
    return -1