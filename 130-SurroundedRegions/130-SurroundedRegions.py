# Last updated: 8/21/2025, 5:06:45 PM
#bfs solution
#search from each matrix boundary cell
#if O is found, start bfs (all O's found from this should be marked special)
#at end, all non special O's are turned to X's


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.xMin = 0
        self.xMax = len(board)-1
        self.yMin = 0
        self.yMax = len(board[0])-1
        #print(self.xMin , self.xMax, self.yMin, self.yMax)
        for i in range(0, len(board)):
            self.bfs([i, self.yMin])
            self.bfs([i, self.yMax])
        for j in range(0, len(board[0])):
            self.bfs([self.xMin, j])
            self.bfs([self.xMax, j])
        self.makeBoardReadyForReturn()
        
    def bfs(self, posn: List[int]):
        if posn[0]<self.xMin or posn[0]>self.xMax or posn[1]<self.yMin or posn[1]>self.yMax:
            return
        #posn we are searching is in bounds
        x = posn[0]
        y = posn[1]
        #print(x,y)
        if self.board[x][y]=='P': #already searched this in prev iteration
            return
        if self.board[x][y]=='X': #cant go here
            return
        if self.board[x][y]=='O':
            self.board[x][y]='P'
            self.bfs([x+1,y])
            self.bfs([x-1,y])
            self.bfs([x, y+1])
            self.bfs([x,y-1])

    def makeBoardReadyForReturn(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                if self.board[i][j]=='P':
                    self.board[i][j]='O'
                else:
                    self.board[i][j]='X'




    
        