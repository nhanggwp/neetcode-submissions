from queue import Queue
class Solution:
    def numIslands( self,grid: List[List[str]]) -> int:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(grid)
        n = len(grid[0])

        q = Queue()
        
        count = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "0"):
                    continue
                count +=1
                q.put((i,j))
                grid[i][j] = "0"
                while(not q.empty()):
                    r,c = q.get()
                    for dir_it in dir:
                        nr,nc = dir_it
                        new_r = r + nr
                        new_c = c + nc
                        if(new_c >= 0 and new_c < n and new_r >= 0 and new_r < m and grid[new_r][new_c] != "0" ):
                            q.put((new_r,new_c))
                            grid[new_r][new_c] = "0"
                    
        return count