bad = 1

def isBadVersion(n):
    return n >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while True:
            if start == end:
                return n
            if isBadVersion(start):
                return start    
            mid = (start + end + 1) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                end = mid 
            else:
                start = mid 



allPass = True
errorMsg = "Value not correct.  Value: {}"

sol = Solution()

vNum = [5, 1, 2, 2, 3, 4]
badV = [4, 1, 2, 1, 3, 2]

# vNum = [4]
# badV = [2]

bad = 4
# result1 = sol.firstBadVersion(5)


try:
    for i in range(len(vNum)):
        bad = badV[i]
        result = sol.firstBadVersion(vNum[i])
        print("Checking result for n = {}, result: {}, bad = {}".format(vNum[i], result, badV[i]))
        assert result == bad, errorMsg.format(result)
except Exception as e: 
    allPass = False
    print("first test failed: {}".format(e))

if allPass:    
    print("Passes all test cases")
