"""
Title: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        if len(nums) > 2:
            for i in range(1, len(nums), 1):
                if nums[i-j] == nums[i-j-1]:
                    nums.remove(nums[i-j])
                    j = j + 1
        elif len(nums) == 2:
            if nums[1] == nums[0]:
                nums.remove(nums[1])
                return 1
        else:
            return 1
            # print(i, j, nums)
        
        return len(nums)