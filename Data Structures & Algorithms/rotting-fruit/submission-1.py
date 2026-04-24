from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(grid) 
        n = len(grid[0])
        q = Queue()
        fresh = 0
        for i in range(m): 
            for j in range(n):
                if (grid[i][j] ==2):
                    q.put((i,j))
                elif (grid[i][j] == 1):
                    fresh += 1
        minutes = 0
        if fresh == 0:
            return 0
        while not q.empty():
            for i in range(q.qsize()):
                r,c = q.get()
                print(r,c)
                for j in dir:
                    nr,nc = j 
                    new_r = r + nr
                    new_c = c + nc
                    if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == 1:
                        fresh -=1 
                        grid[new_r][new_c] =2
                        q.put((new_r,new_c))
            minutes +=1
        
        return minutes -1 if fresh == 0 else -1