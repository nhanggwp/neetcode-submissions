from typing import List
from queue import Queue
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_pacific(i,j):
            return i == 0 or j == 0
        def is_alantic(i,j,m,n):
            return  i == m -1 or j == n -1 
        m = len(heights)
        n = len(heights[0])
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        ans = []
    
        for i in range(m):
            for j in range(n):
                stack = [] 
                stack.append((i,j))
                pacific_check = is_pacific(i,j)
                atlantic_check = is_alantic(i,j,m,n)
                visited = set()
                visited.add((i,j))
                while(len(stack) != 0):
                    node_r,node_c = stack.pop()
                    for dir_it in dir:
                        nr,nc = dir_it
                        new_node_r = node_r + nr
                        new_node_c  = node_c + nc
                        if( new_node_c >= 0 and new_node_c < n and new_node_r >= 0 and new_node_r < m and heights[new_node_r][new_node_c] <= heights[node_r][node_c] and (new_node_r,new_node_c) not in visited):
                            stack.append((new_node_r,new_node_c)) 
                            visited.add((new_node_r,new_node_c))
                            if(is_pacific(new_node_r,new_node_c)):
                                pacific_check = True
                            if(is_alantic(new_node_r,new_node_c,m,n)):
                                atlantic_check = True
                        if(pacific_check and atlantic_check):
                            break
                if(pacific_check and atlantic_check):
                    ans.append((i,j))

                
        return ans 