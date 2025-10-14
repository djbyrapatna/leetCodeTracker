# Last updated: 10/14/2025, 2:30:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head.next == None:
        #     return None
        nodesSeen = 1
        curr = head
        nthNode = curr
        before = None
        while curr.next is not None:
            #advance curr
            #if we have seen less than n nodes keep nthNode at start
            #once we see n nodes start advancing nthNode concurrently
            curr = curr.next
            nodesSeen+=1
            if nodesSeen > n:
                before = nthNode
                nthNode = nthNode.next
        if before == None:
            return nthNode.next
        else:
            
            before.next = nthNode.next
            return head