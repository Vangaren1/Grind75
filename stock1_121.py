from typing import List

"""
Below is the leetcode solution

"""
  
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestPrice =  10**5 
        for i in range(len(prices)):
            currPrice = prices[i]
            if currPrice < lowestPrice:
                lowestPrice = currPrice
            prof = currPrice - lowestPrice
            if prof > profit:
                profit = prof
        return profit
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    errorMsg = "Value not correct, {}"
    
    allPass = True
    
    prices = [7,1,5,3,6,4]
    result1 = s.maxProfit(prices)
    try:
        assert result1 == 5, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))
    
    prices = [7,6,4,3,1]
    result2 = s.maxProfit(prices)
    
    try: 
        assert result2 == 0, errorMsg.format(result2)
    except Exception as e:
        allPass = False
        print("second test failed: {}".format(e))
    # result1 = s.twoSum([2,7,11,15], 9)
    # assert result1 == [0,1] , errorMsg

    if allPass:    
        print("Passes all test cases")
    