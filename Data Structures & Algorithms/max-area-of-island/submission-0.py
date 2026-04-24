from typing import List
from queue import Queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        q = Queue()
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    continue
                area = 0
                q.put((i,j))
                while(not q.empty()):
                    node_r,node_c = q.get()
                    area += 1
                    grid[node_r][node_c] =0
                    for dir_it in dir:
                        n_r , n_c = dir_it
                        new_r = node_r + n_r
                        new_c = node_c + n_c
                        if new_c >= 0 and new_c < n and new_r >= 0 and new_r < m and grid[new_r][new_c] != 0:
                            q.put((new_r,new_c))
                            grid[new_r][new_c] = 0
                max_area = max(area,max_area)
            
        return max_area