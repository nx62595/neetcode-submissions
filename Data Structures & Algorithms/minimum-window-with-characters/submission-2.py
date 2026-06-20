class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0 
        t_hash = set(t)

        ind_hash = {}
        for c in t:
            ind_hash[c] = ind_hash.get(c, 0) + 1

        win_hash = {}
        res_len = len(s) + 1

        res = ""
        for r in range(len(s)):
            win_hash[s[r]] = win_hash.get(s[r], 0) + 1
            while all(win_hash.get(k, 0) >= v for k, v in ind_hash.items()):
                if r - l + 1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                win_hash[s[l]] -= 1
                l += 1

        return res
