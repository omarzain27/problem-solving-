# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev = None
        curr = head
        result = 0
        i = 0
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while prev:
            result += prev.val *pow(2,i)
            i +=1
            prev =prev.next
        return result
            
        