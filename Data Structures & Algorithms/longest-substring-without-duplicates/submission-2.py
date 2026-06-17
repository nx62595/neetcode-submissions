class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_sub = {}
        max_length = 0
        initial = 0
        for i in range(len(s)):
            if s[i] in curr_sub:
                initial = max(curr_sub[s[i]] + 1,initial)
            curr_sub[s[i]] = i
            max_length = max(max_length, i - initial + 1)

        return max_length