from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            requirements[course].append(pre)
        visited = set()

        def bfs(course):
            if course in visited:
                return False
            if requirements.get(course) == []:
                return True
            visited.add(course)
            for pre in requirements.get(course):
                if not bfs(pre):
                    return False
            requirements[course] = []
            visited.remove(course)
            return True
        for c in range(numCourses):
            if not bfs(c): return False
        return True
        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    numCourses = 4
    prerequisites = [ [0,1], [1,2], [2,3]]

    result1 = sol.canFinish(numCourses, prerequisites)
    expected = True

    try:
        assert result1 == 5, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    