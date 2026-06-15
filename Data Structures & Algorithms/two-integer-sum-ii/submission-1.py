class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = {}
        for i in range(len(numbers)):
            if numbers[i]  not in num_set:
                nums2 = target - numbers[i]
                if nums2 in num_set:
                    return [num_set[nums2], i + 1]
                num_set[numbers[i]] = i + 1
