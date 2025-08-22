# Last updated: 8/21/2025, 9:34:59 PM
from collections import deque
class Solution:
    # numCourses
    # adjMatrix
    # noIncomingQueue
    # sums

    def buildAdjacencyListAndQueue(self, prerequisites: List[List[int]]):
        self.adjMatrix = [[0]*self.numCourses for i in range(self.numCourses)]
        self.sums = [0]*self.numCourses
        for link in prerequisites:
            i = link[0]
            j = link[1]
            self.adjMatrix[i][j]=1
        for i in range(self.numCourses):
            self.sums[i] = sum(self.adjMatrix[i])


        self.noIncomingQueue = deque([])
        for i in range(self.numCourses):
            if self.sums[i]==0:
                self.noIncomingQueue.append(i)

    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        self.numCourses = numCourses
        self.buildAdjacencyListAndQueue(prerequisites)
        nodesSorted = 0

        while(self.noIncomingQueue):
            node = self.noIncomingQueue.popleft()
            nodesSorted+=1
            for i in range(self.numCourses):
                if(self.adjMatrix[i][node]==1):
                    self.adjMatrix[i][node]=0
                    self.sums[i]-=1
                    if self.sums[i]==0:
                        self.noIncomingQueue.append(i)
        

        return nodesSorted==self.numCourses

        