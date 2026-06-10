class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tbl = {}
        for i in nums:
            if i in tbl:
                tbl[i] += 1
            else:
                tbl[i] = 1

            
        sorted_tbl = sorted(tbl, key=tbl.get)
        print(sorted_tbl)

        return list(sorted_tbl[-k:])
        
        