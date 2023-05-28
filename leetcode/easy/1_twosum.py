'''
LeetCode link: https://leetcode.com/problems/two-sum/

Problem description:
--------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

example - 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

example - 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

example - 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
'''

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    mem = {}    # at each iteration, save the number and index for lookup. Possible only because of constraint - 'Only one valid answer exists.'
    for idx in range(len(nums)):
        compliment = target-nums[idx]   
        if compliment in mem:   # check if current number's compliment occured so far. If yes, return compliment's idx, current idx [both values at these positions sums to target]
            return [mem[compliment], idx]
        mem[nums[idx]] = idx    # if not present, add current number and idx to lookup in the future

    return []       # if no solution found return empty. Ideally shouldn't happen according to the last constraint

# test

assert twoSum([2,7,11,15],9) == [0,1]
assert twoSum([3,2,4],6) == [1,2]
assert twoSum([3,3],6) == [0,1]
assert twoSum([9,9,9,9,9],18) == [0,1]
assert twoSum([2,7,11,15],90) == []
