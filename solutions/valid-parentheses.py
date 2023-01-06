"""
Title: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/submissions/871352608/
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openen = '([{'
        closen = ')]}'

        parenthes = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        lstopen = []
        for i in s:
            if i in openen:
                lstopen.append(parenthes[i])
            elif len(lstopen) > 0:
                if i == lstopen[-1]:
                    lstopen = lstopen[:-1]
                else:
                    return False
            else:
                return False
            # print(i, lstopen)
        if len(lstopen) == 0:
            return True
        else:
            return False