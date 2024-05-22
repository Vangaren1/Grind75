from typing import List

"""
Below is the leetcode solution

"""
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def isValid(x,y):
            return 0 <= x < maxX and 0 <= y < maxY
        oldColor = image[sc][sr]
        maxX = len(image)
        maxY = len(image[0])
        visited = set()            
        toVisit = [(sc,sr)]

        while toVisit:
            x,y = toVisit.pop()
            image[x][y] = color
            visited.add((x,y))
            toCheck = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            for check in toCheck:
                a, b = check
                if isValid(a,b):
                    if image[a][b] == oldColor and (a,b) not in visited:
                        toVisit.append((a,b))
        return image

        
        
        
                
        pass 
        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct"
    
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    
    result1 = sol.floodFill(image, sr, sc, color)
    
    output1 = [[2,2,2],[2,2,0],[2,0,1]]
    
    try:
        assert result1 == output1, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    