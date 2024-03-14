"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Input: x = -123
Output: -321
"""

def reverse(self, x: int) -> int:

        reversed_num = str(x)
        negative = False

        if reversed_num[0] == '-':
            negative =True
            reversed_num = reversed_num[1:]
        reversed_num = reversed_num[::-1]

        if negative:
            reversed_num = '-' + reversed_num
        reversed_num = int(reversed_num) 

        if -2**31 <= reversed_num & reversed_num <= 2**31 - 1:
            return reversed_num

        return 0
  
