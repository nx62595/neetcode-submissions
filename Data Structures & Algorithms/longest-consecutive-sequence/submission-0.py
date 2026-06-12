class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        res = 1
        nums_set = set(nums)

        for i in nums_set:
            if i - 1 in nums_set: continue
            j = 0
            while j + i in nums_set:
                j += 1

            if j > res:
                res = j

        return res 