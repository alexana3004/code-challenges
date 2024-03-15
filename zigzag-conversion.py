"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        output = ''
        r = 1
        while r <= numRows and r < len(s) + 1:   
            i = r - 1
            output += s[i]
            while i < len(s):
                next_i = i
                if numRows - r > 0:
                    next_i += (numRows - r) * 2
                    if next_i < len(s):
                        output += s[next_i]
                    
                if r - 1 > 0:
                    next_i += (r - 1) * 2
                    if next_i < len(s):
                        output += s[next_i]
                i = next_i
            r += 1

        return output
