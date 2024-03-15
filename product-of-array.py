"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
        from numpy import prod

        answer = []
        map_prod = {}
        if nums.count(0) > 1:
            return [0] * len(nums)
        elif nums.count(0) == 1:
            answer = [0] * len(nums)
            i = nums.index(0)
            nums.pop(i)
            answer[i] = prod(nums)
            return answer
          
        for i in range(len(nums)):
            if nums[i] in map_prod:
                product = map_prod.get(nums[i])
            else:
                n = list(nums)
                n.pop(i)
                product = prod(n)
                map_prod[nums[i]] = product
            answer.append(product)

        return answer
