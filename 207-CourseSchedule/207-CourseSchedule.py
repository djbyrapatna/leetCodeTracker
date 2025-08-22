# Last updated: 8/21/2025, 9:39:14 PM
from collections import deque, defaultdict
class Solution:
    # numCourses
    # adjMatrix
    # noIncomingQueue
    # sums

    def buildAdjacencyListAndQueue(self, prerequisites: List[List[int]]):
        self.graph = defaultdict(list)
        self.indegree = [0] * self.numCourses

        for ai, bi in prerequisites:
            self.graph[bi].append(ai)
            self.indegree[ai] += 1

        self.noIncomingQueue = deque([])
        for i in range(self.numCourses):
            if self.indegree[i]==0:
                self.noIncomingQueue.append(i)
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        self.numCourses = numCourses
        self.buildAdjacencyListAndQueue(prerequisites)
        nodesSorted = 0

        while(self.noIncomingQueue):
            node = self.noIncomingQueue.popleft()
            nodesSorted+=1
            for nei in self.graph[node]:
                self.indegree[nei]-=1
                if self.indegree[nei]==0:
                    self.noIncomingQueue.append(nei)
                    
        

        return nodesSorted==self.numCourses

        