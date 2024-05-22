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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()

        ptr = newHead
        
        # combine both till 1 is empty
        while list1 and list2:
            tmp = ListNode()
            if list1.val <= list2.val:
                tmp.val = list1.val
                list1 = list1.next
            else:
                tmp.val = list2.val
                list2 = list2.next
            ptr.next = tmp
            ptr = ptr.next

        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        
        return newHead.next
        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    errorMsg = "Value not correct"
    
    # 1,2,3     1,3,4
    list1 = ListNode()
    list1.val = 1
    list1.next = ListNode()
    list1.next.val = 2
    list1.next.next = ListNode()
    list1.next.next.val = 4
    
    list2 = ListNode()
    list2.val = 1
    list2.next = ListNode()
    list2.next.val = 3
    list2.next.next = ListNode()
    list2.next.next.val = 4
    
    newList = s.mergeTwoLists(list1, list2)
    
    while newList:
        print(newList.val)
        newList = newList.next
    
    # result1 = s.twoSum([2,7,11,15], 9)
    # assert result1 == [0,1] , errorMsg
    
    print("Passes all test cases")
    