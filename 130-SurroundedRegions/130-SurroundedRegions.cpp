// Last updated: 8/21/2025, 5:23:08 PM
class Solution {
public:
    int xMin;
    int xMax;
    int yMin;
    int yMax;

    
    void solve(vector<vector<char>>& board) {
        xMin = 0;
        yMin = 0;
        xMax = board.size()-1;
        yMax = board[0].size()-1;
        
        

        for(size_t i =0; i <= xMax; i++){
            bfs(board, i, yMin);
            bfs(board, i, yMax);
        }
        for(size_t j =0; j <= yMax; j++){
            bfs(board, xMin, j);
            bfs(board, xMax, j);
        }
        prepBoard(board);

    }

    void bfs(vector<vector<char>>& board, int x, int y){
        if (x < 0 || x> xMax || y < 0 || y > yMax){
            return; //out of bounds
        }
        if (board[x][y]=='P' || board[x][y]=='X'){
            //been here or cant go here
            return;
        }
        if(board[x][y]=='O'){
            board[x][y]='P';
            bfs(board, x-1, y);
            bfs(board, x+1,y);
            bfs(board, x, y-1);
            bfs(board, x, y+1);
        }
        return;
    }

    void prepBoard(vector<vector<char>>& board){
        for(size_t i =0; i<=xMax; i++){
            for(size_t j=0; j <= yMax; j++){
                if(board[i][j]=='P'){
                    board[i][j]='O';
                } else{
                    board[i][j]='X';
                }
            }
        }
    }
};