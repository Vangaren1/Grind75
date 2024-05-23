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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        ptr1 = head
        ptr2 = head
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr2 is None:
                break
        return ptr1 
    
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
        head.next = ListNode(i)
        head = head.next

    expected = ptr.next.next


    result1 = sol.middleNode(ptr)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    head = ListNode(1)
    ptr = head
    for i in range(2,7):
        head.next = ListNode(i)
        head = head.next
        
    expected = ptr.next.next.next

    result1 = sol.middleNode(ptr)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    