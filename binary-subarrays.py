"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

Constraints:
1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
"""

def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        if nums.count(1) >= goal:
            output = 0
            for n in range(len(nums)):
                sum = nums[n]
                if sum == goal:
                    output += 1
                if n < len(nums) - 1:
                    for i in range(n + 1, len(nums)):
                        sum += nums[i]
                        if sum == goal:
                            output += 1
                        elif sum > goal:
                            break
        else:
            return 0

        return output
  
