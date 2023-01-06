"""
Title: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/description/
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = list(set(nums))
        if len(nums) == len(nums_set):
            return False
        else:
            return True