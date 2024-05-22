class Solution:
    stairDict = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.stairDict:
            return self.stairDict.get(n)
        steps = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.stairDict[n] = steps
        return steps 

steps = [2,3,4, 10]
out = [2,3, 5, 10]

allPass = True
errorMsg = "Value not correct, Value: {}"

sol = Solution()

for i in range(len(steps)):
    result = sol.climbStairs(steps[i])
    try:
        assert result == out[i], errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("test failed: {}".format(e))
    
if allPass:    
    print("Passes all test cases")