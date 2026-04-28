from queue import Queue

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = Queue()

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    q.put((i,j))
                else:
                    continue

        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        while(not q.empty()):
            for i in range(q.qsize()):
                node_r,node_c = q.get()
                for dir_r,dir_c in dir:
                    new_r =  node_r + dir_r
                    new_c = node_c + dir_c
                    if( new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] != -1 ):
                        if(grid[node_r][node_c] + 1 < grid[new_r][new_c]):
                            grid[new_r][new_c] = grid[node_r][node_c] + 1
                            q.put((new_r,new_c))
                        else:
                            continue
                    else:
                        continue
    