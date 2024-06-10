from typing import List, Optional
"""
Below is the leetcode solution

"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = []
        height = len(mat)
        width = len(mat[0])
        
        hashCount = 0
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] != 0:
                    mat[i][j] = '#'
                    hashCount += 1
                else:
                    q.append((i,j))
        
        while hashCount > 0:
            x,y = q.pop(0)
            for dx, dy in [ (1,0), (-1,0), (0,1) , (0,-1)]:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < height and 0 <= ny < width and mat[nx][ny] == '#':
                    mat[nx][ny] = 1 + mat[x][y]
                    hashCount -= 1
                    q.append((nx,ny))
        
        return mat    
        
        
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    mat = [[0,1,1],[1,1,1],[1,1,1]]
    Output = [[0,0,0],[0,1,0],[1,2,1]]
    
    result1 = sol.updateMatrix(mat)
    
    try:
        assert result1 == Output, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    