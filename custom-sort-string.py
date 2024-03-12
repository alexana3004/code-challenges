"""
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should
occur before y in the permuted string.
Return any permutation of s that satisfies this property.

Constraints:
1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.

Input:  order = "bcafg", s = "abcd" 
Output:  "bcad"
"""


class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        common_char = [c for c in order if c in s]
        uncommon_char = [c for c in s if c not in order]
        ordered_str = []
        for c in common_char:
            c = c * s.count(c)
            ordered_str.append(c) 
        ordered_str += uncommon_char
        return ''.join(ordered_str)
