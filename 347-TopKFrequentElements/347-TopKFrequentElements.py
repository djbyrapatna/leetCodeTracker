# Last updated: 10/14/2025, 5:42:29 PM
import heapq
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        #heapq.heapify(pq)
        ctr = Counter(nums)
        mc = ctr.most_common(k)
        return [x for [x,y] in mc]
        #dc = defaultdict(int)
        # for num in nums:
        #     dc[num]+=1
        # for key in dc.keys():
        #     val = dc[key]
        #     heapq.heappush(pq,(-val,key))

        # retList = [0]*k
        # for i in range(k):
        #     _, elem = heapq.heappop(pq)
        #     retList[i] = elem
        # return retList
        
        