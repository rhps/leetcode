"""
Title: 209. Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        tot = 0
        res = float("inf")
        while right < len(nums):
            print(right, left, tot, res)
            r = nums[right]
            tot = tot + r
            right += 1
            while tot >= target:
                res = min(res, right - left)
                tot = tot - nums[left]
                left += 1
        return res if res < float("inf") else 0