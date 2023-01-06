"""
Title: 704. Binary Search
Link: https://leetcode.com/problems/binary-search/description/
"""
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 1:
            low = low - 1
            
        if high % 2 == 1:
            high = high + 1
            
        return (high - low)//2