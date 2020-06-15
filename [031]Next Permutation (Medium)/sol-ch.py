class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Reference: https://stackoverflow.com/questions/1622532/algorithm-to-find-next-greater-permutation-of-a-given-string
        if len(nums) >= 2:
            i = len(nums) - 2
            while nums[i] >= nums[i + 1]:
                if i == 0:
                    break
                else:
                    i -= 1

            j = len(nums) - 1

            while nums[i] >= nums[j]:
                if j == 0:
                    break
                else:
                    j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            if (i == 0) and (j == 0):
                nums[:] = sorted(nums)
            else:
                nums[i + 1:] = sorted(nums[i + 1:])