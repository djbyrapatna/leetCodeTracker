# Last updated: 10/14/2025, 1:34:15 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not curr:
            return None
        nxt = curr.next
        counter = 0
        curr.next = None
        
        while nxt:
            
            
            nxt2 = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = nxt2
        return curr


        