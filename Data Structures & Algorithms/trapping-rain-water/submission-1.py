class Solution:
    def trap(self, height: List[int]) -> int:
        total_volume = 0
        n = len(height)
        left_max =  [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        l, r = 1, n - 2
        while l < n and r > -1:
            left_max[l] = max(height[l], left_max[l-1])
            right_max[r] = max(height[r], right_max[r+1])

            l += 1
            r -= 1

        for i in range(n):
            total_volume += min(left_max[i], right_max[i]) - height[i]
        return total_volume
        
