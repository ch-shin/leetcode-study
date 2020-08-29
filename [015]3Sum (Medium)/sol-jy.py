class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, tmp_res = set(), ()
        srt_nums = sorted(nums)
        print(srt_nums)
                       
        for fixed in range(len(nums)):
            target = srt_nums[fixed]
            idx_1, idx_2 = fixed+1, len(nums)-1
            
            while idx_1 < idx_2:
                num_1, num_2 = srt_nums[idx_1], srt_nums[idx_2]
                if num_1 + num_2 < -target:
                    idx_1 += 1
                elif num_1 + num_2 > -target:
                    idx_2 -= 1
                else:
                    tmp_res = (target, num_1, num_2)
                    #print(tmp_res)
                    res.add(tmp_res)
                    idx_1 += 1
            
        print(res)
                       
        return res
