"""
Title: 1480. Running Sum of 1d Array
Link: https://leetcode.com/problems/running-sum-of-1d-array/description/
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        num_ln = len(nums)

        for i in range(num_ln-1, -1, -1):
            result = 0
            for j in range(num_ln-i):
                result = result + nums[j]
            res.append(result)
        
        return res