"""
Title: 1491. Average Salary Excluding the Minimum and Maximum Salary
Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
"""
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        avg = sum(sorted(salary)[1:-1])
        return float(avg)/(len(salary)-2)