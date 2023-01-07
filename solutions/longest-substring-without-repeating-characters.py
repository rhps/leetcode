"""
Title: 3. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = collections.Counter()

        left, right = 0, 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res