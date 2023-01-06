"""
Title: 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/description/
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False