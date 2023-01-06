"""
Title: 13. Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/description/
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        s = list(s)
        tot = roman[s[0]]

        for i in range(1, len(s), 1):
            print(tot)
            if roman[s[i-1]] < roman[s[i]] :
                tot = tot + roman[s[i]] - roman[s[i-1]] - roman[s[i-1]]
            else:
                tot = tot + roman[s[i]]
        print(tot)
        return tot