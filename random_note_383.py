from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mDict = defaultdict(int)
        for m in magazine:
            mDict[m] += 1

        rDict = defaultdict(int)
        for r in ransomNote:
            rDict[r] += 1

        for r in rDict:
            if rDict[r] > mDict[r]:
                return False
        
        return True

sol = Solution()

ransomNote = "a"
magazine = "b"
output = False

print(sol.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
output = True

print(sol.canConstruct(ransomNote, magazine))