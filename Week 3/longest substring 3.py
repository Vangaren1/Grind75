from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLen = 0

        index = 0
        length = len(s)
        start = 0
        while index < length:
            char = s[index]
            if char not in seen:
                seen.add(char)
                
            else:
                while char in seen:
                    tmp = s[start]
                    seen.remove(tmp)
                    start += 1                
                seen.add(char)
            index += 1
            maxLen = max( maxLen, index - start)
        return maxLen

    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    s = ["abcabcbb", "bbbbb", "pwwkew"]
    expected = [3,1,3]

    for string in range(len(s)):
        result = sol.lengthOfLongestSubstring(s[string])    
        try:
            assert result == expected[string], errorMsg.format(result)
        except Exception as e: 
            allPass = False
            print("{} test failed: {}".format(string, e))

    if allPass:    
        print("Passes all test cases")
    