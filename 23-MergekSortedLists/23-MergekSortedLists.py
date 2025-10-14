# Last updated: 10/14/2025, 1:56:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        if not curr1:
            return list2
        curr2 = list2
        if not curr2:
            return list1
        retHead = None
        curr = None
        if curr1.val<=curr2.val:
            retHead = curr1
            curr1 = curr1.next
            curr = retHead
        else:
            retHead = curr2
            curr2 = curr2.next
            curr = retHead
        
        while curr1 != None or curr2 !=None:
            if curr1 == None:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
            elif curr2 == None:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            else:
                if curr1.val<=curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                    curr = curr.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                    curr = curr.next
        return retHead


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            
            return None
        if k == 1:
            return lists[0]
        if k == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            k2 = k//2
            leftMerge = self.mergeKLists(lists[0:k2])
            rightMerge = self.mergeKLists(lists[k2:])
            return self.mergeTwoLists(leftMerge, rightMerge)
        