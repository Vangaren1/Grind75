from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minMap = [ amount + 1 for _ in range(amount+1)]
        minMap[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0 :
                    minMap[i] = min(minMap[i], minMap[i - c] + 1 )
        return minMap[amount] if minMap[amount] != amount + 1 else -1


    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    coins = [186,419,83,408]
    amount = 6249
    expected = 20

    result1 = sol.coinChange(coins, amount)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    