"""
Title: 88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/submissions/872992368/
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[0:n]
        return nums1.sort()