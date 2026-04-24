class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        if len(edges) != n -1:
            return False
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a,b):
            parent_A = find(a)
            parent_B = find(b)

            if parent_A == parent_B:
                return True
            
            parent[parent_B] = parent_A
            return False
        
        for a,b in edges:
            if union(a,b):
                return False
        
        return True

