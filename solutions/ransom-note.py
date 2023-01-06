"""
Title: 383. Ransom Note
Link: https://leetcode.com/problems/ransom-note/submissions/869850210/
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True
        else:
            for n in ransomNote:
                if n in magazine:
                    magazine = magazine.replace(n, '', 1)
                else:
                    return False
            return True