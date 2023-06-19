"""
LeetCode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem description:
--------------------
You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

example - 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

example - 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    
Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    l,p = 0,0           # initialize left pointer and profit to 0
    for r in range(len(prices)):        # iterate the right pointer - O(n)
        if prices[r] < prices[l]:       # if right (future) price is lower than current price, move left pointer (change buy price to lower value)
            l=r
        else:
            p = max(p, prices[r]-prices[l])     # if not, calculate the current profit and set final profit to max of current and past profit
    return p


    
# test
assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
assert maxProfit([0]) == 0
assert maxProfit([7]) == 0
assert maxProfit([7,2,10,1,9,2]) == 8
