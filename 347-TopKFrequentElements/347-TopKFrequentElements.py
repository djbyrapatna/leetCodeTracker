# Last updated: 10/14/2025, 3:03:28 PM
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        heapq.heapify(pq)
        dc = defaultdict(int)
        for num in nums:
            dc[num]+=1
        for key in dc.keys():
            val = dc[key]
            heapq.heappush(pq,(-val,key))

        retList = [0]*k
        for i in range(k):
            _, elem = heapq.heappop(pq)
            retList[i] = elem
        return retList
        
        