from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        height  = len(mat)
        width = len(mat[0])

        for i in range(height):
            for j in range(width):
                if mat[i][j] != 0:
                    mat[i][j] = '#'
                else:
                    queue.append((i,j))
        
        for row, column in queue:
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = row + dx 
                nc = column + dy

                if 0 <= nr < height and 0 <= nc < width and mat[nr][nc] == '#':
                    mat[nr][nc] = 1 + mat[row][column]
                    queue.append((nr,nc))
                    
        return mat

        
        
                
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
        
    # mat = [[0,0,0],[0,1,0],[0,0,0]]
    # Output= [[0,0,0],[0,1,0],[0,0,0]]

    # result1 = sol.updateMatrix(mat)
    
    # try:
    #     assert result1 == Output, errorMsg.format(result1)
    # except Exception as e: 
    #     allPass = False
    #     print("first test failed: {}".format(e))

        
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output = [[0,0,0],[0,1,0],[1,2,1]]

    result1 = sol.updateMatrix(mat)
    
    try:
        assert result1 == Output, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))


    if allPass:    
        print("Passes all test cases")
    