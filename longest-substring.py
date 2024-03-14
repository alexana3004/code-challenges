"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        longest_substring = ''
        for char in s:
            if char not in substring:
                substring += char
                if len(substring) > len(longest_substring):
                    longest_substring = substring
            else:
                substring = substring[substring.index(char) + 1 :] + f'{char}' 
        return len(longest_substring)
  
