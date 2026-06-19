class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tbl = {}
        l, r = 0, 0
        for c in s1:
            tbl[c] = tbl.get(c,0) + 1

        for r in range(len(s2)):
            tbl[s2[r]] = tbl.get(s2[r],0) - 1
            while tbl.get(s2[r], 0) < 0:
                tbl[s2[l]] += 1
                l += 1
           
            if r - l + 1 == len(s1):
                return True
        return False