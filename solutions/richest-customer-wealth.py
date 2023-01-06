"""
Title: 1672. Richest Customer Wealth
Link: https://leetcode.com/problems/richest-customer-wealth/description/
"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for account in accounts:
            tot_money = 0
            for money in account:
                tot_money = tot_money + money
            
            if tot_money > highest:
                highest = tot_money

        return highest