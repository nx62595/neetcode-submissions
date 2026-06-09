class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            sec_nums = target - nums[i]
            if sec_nums in hashset:
                return[hashset[sec_nums], i]
            else:
                hashset[nums[i]] = i