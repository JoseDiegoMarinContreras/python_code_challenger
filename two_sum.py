"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return hash_map[target - num], i
        hash_map[nums[i]] = i

#(0, 1)
print(twoSum([2,7,11,15], 9))
#(1, 2)
print(twoSum([3,2,4], 6))
#(0, 1)
print(twoSum([3,3], 6))