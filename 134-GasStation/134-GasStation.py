# Last updated: 10/9/2025, 7:59:21 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        N = len(gas)
        
        testArr = [0]*N
        testArr[0] = gas[0] - cost[0]
        minValue = testArr[0]
        minIndex = 0
        for i in range(1, N):
            testArr[i] = testArr[i-1]+gas[i]-cost[i]
            if testArr[i]<minValue:
                minValue = testArr[i]
                minIndex = i



        if testArr[-1]<0:
            return -1
        elif minIndex == N-1:
            return 0
        else:
            return minIndex+1
        



                
        