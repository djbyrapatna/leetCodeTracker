# Last updated: 10/14/2025, 1:44:22 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #rabbit and turtle approach
        if not head:
            return False
        rabbitCurr = head
        turtleCurr = head

        print(rabbitCurr==turtleCurr)
        

        turtleNext = head.next
        if not turtleNext:
            return False
        rabbitNext = rabbitCurr.next.next
        #counter = 0

        while rabbitNext != None and turtleNext != None:
            #counter+=1
            rabbitCurr = rabbitNext
            turtleCurr = turtleNext
            # print(rabbitCurr.val, turtleCurr.val, rabbitCurr==turtleCurr)
            if rabbitCurr == turtleCurr:
                return True
            turtleNext = turtleCurr.next
            if not turtleNext:
                return False
            if not rabbitCurr.next:
                return False
            rabbitNext = rabbitCurr.next.next
        
        return False





