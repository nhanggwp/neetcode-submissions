class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        marked = [[0] * n for _ in range(m) ]
        dq = deque()
        for i in range(m):
            if board[i][0] == "O":
                dq.append((i,0))
                marked[i][0] = 1
            if board[i][n-1] == "O":
                dq.append((i,n-1))
                marked[i][n-1] = 1

        for j in range(n):
            if board[0][j] == "O":
                dq.append((0,j))
                marked[0][j] = 1
            if board[m-1][j] == "O":
                dq.append((m-1,j))
                marked[m-1][j] = 1
        dir = [[0,1], [1,0], [0,-1], [-1,0]]

        while dq:
            node_r,node_c = dq.popleft()
            for dir_r,dir_c in dir:
                new_r = node_r + dir_r
                new_c = node_c + dir_c
                if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and marked[new_r][new_c] == 0 and board[new_r][new_c] == "O":
                    dq.append((new_r,new_c))
                    marked[new_r][new_c] = 1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and marked[i][j] == 0:
                    board[i][j] = "X"
            