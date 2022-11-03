#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'Ashish Rai'
__copyright__ = 'Copyright 2022, Ashish Rai'
__credits__ = ['Ashish Rai']
__license__ = 'Public Domain'
__email__ = 'je.suis.ashishrai@gmail.com'
__date__ = '03/11/2022'

"""
Two Sums
========

Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to
`target`.

You may assume that each input would have exactly one solution,
and you may not use the same element twice

Example 1:

    Input: nums = [2, 7, 11, 15], Target= 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9

Example 2:

    Input: nums = [3, 2, 4], Target = 6
    Output: [1, 2]
    Explanation: Because nums[1] + nums[2] == 6

Constraints:

    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists

TODO:
    - Take inputs from command line
"""

if __name__ == "__main__":
    class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            for j in range(len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[j] + nums[k] == target: return [j, k]
