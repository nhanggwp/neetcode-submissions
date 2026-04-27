class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a,b):
            nonlocal count
            node_a = find(a)
            node_b = find(b)
            if node_a != node_b:
                count = count -1
                parent[node_b] = node_a
        
        for a,b in edges:
            union(a,b)
        
        return count


