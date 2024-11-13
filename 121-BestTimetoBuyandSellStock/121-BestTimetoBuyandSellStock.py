class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        opt = [[0]*2 for _  in range(n)]
        opt[0][0] = prices[0]
        opt[0][1] = float('-inf')
        for i in range(1,n):
            opt[i][0] = min(opt[i-1][0],prices[i])
            opt[i][1] = max(prices[i]-opt[i-1][0], opt[i-1][1])
        maxProfit = int(opt[-1][1])
        return max(maxProfit,0)

        