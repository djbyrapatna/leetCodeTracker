# Last updated: 10/14/2025, 4:23:39 PM
from collections import deque, defaultdict
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasksDone = 0
        # taskOrder = []
        # startTime = 10**9+1
        # endTime= 0
        # for i, task in enumerate(tasks):
        #     enqTime = task[0]
        #     if enqTime < startTime:
        #         startTime = enqTime
        #     if enqTime > endTime:
        #         endTime = enqTime
        
        #turn tasks array into priority queue where priority is enq time, also store processing time, index
        #1. pop to get lowest enq time (continue pop till next is higher enq time)
        #2. for each pop add to (processing time, index) priority queue
        #3. pop lowest proc time from 2nd priority queue, add index to final order, bump curr time, then repeat 1 2 3 (on 1, pop till next is higher than curr tyime)
        tasksInd = list(enumerate(tasks))
        tasksAug = [ (y,z,x) for (x, [y,z]) in tasksInd]
        heapq.heapify(tasksAug)
        processingTimeQueue = []
        heapq.heapify(processingTimeQueue)
        currTime, t1, t2 = heapq.heappop(tasksAug)
        heapq.heappush(tasksAug, (currTime,t1,t2))
        tasksOrder = []
        while tasksAug or processingTimeQueue:
           
            while tasksAug:
                enqTime, proc, ind = heapq.heappop(tasksAug)
                if enqTime > currTime:
                    if processingTimeQueue: #at current time, we have unprocessed tasks, we push this back on and continue to processing stage
                        heapq.heappush(tasksAug, (enqTime, proc, ind) )
                        break
                    else: #else, jump to this time
                        heapq.heappush(processingTimeQueue, (proc, ind))
                        currTime = enqTime
                else:
                    heapq.heappush(processingTimeQueue, (proc, ind))
            
            leastProc, ind = heapq.heappop(processingTimeQueue)
            tasksOrder.append(ind)
            currTime +=leastProc
        
        return tasksOrder
        