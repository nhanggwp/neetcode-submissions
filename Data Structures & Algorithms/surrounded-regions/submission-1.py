class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        marked = [[0] * n for _ in range(m) ]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m -1 or j == n - 1:
                    if board[i][j] == "O":
                        marked[i][j] = 1
                        dq.append((i,j))
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
            