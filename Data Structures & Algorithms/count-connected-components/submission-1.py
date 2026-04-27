class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a,b):
            node_a = find(a)
            node_b = find(b)
            if node_a != node_b:
                parent[node_b] = node_a
        
        for a,b in edges:
            union(a,b)
        component = set ()
        for i in range(0,n):
            component.add(find(i))
        
        return len(list(component))


