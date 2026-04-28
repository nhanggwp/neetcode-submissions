class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vertices = set()
        for a,b in edges:
            vertices.add(a)
            vertices.add(b)
        
        n = len(list(vertices))

        parent = [i for i in range(n+1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        def union(a,b):
            node_a = find(a)
            node_b = find(b)
            
            if(node_a == node_b):
                return True
            parent[node_b] = node_a
            return False
        
        for a,b in edges:
            if (union(a,b)):
                return [a,b]
        
        return []
            
