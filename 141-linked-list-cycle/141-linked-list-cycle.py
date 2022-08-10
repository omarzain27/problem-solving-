# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = head
        tail = dummy
        cnt = 10004
        while cnt:
            if tail == None :
                return False
            tail = tail.next
            cnt-=1
        return True