from typing import List, Optional

"""
Below is the leetcode solution

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        stack = []
        while head:
            stack.insert(0, head)
            head = head.next
        for i in range(len(stack)-1):
            stack[i].next = stack[i+1]
        stack[-1].next = None
        return stack[0]
            
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    head = ListNode(1)
    ptr = head
    for i in range(2,6):
        ptr.next = ListNode(i)
        ptr = ptr.next   
    
    result1 = sol.reverseList(head)
    
    while result1:
        print(result1.val)
        result1 = result1.next
    
    # try:
    #     assert result1 == 5, errorMsg.format(result1)
    # except Exception as e: 
    #     allPass = False
    #     print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    