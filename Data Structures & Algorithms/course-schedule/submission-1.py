class Solution:
   def canFinish(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for a,b in prerequisites:
            graph[a].append(b)

        path = set()
        visted = set ()

        def dfs(course):
            if course in path:
                return False
            
            if course in visted:
                return True

            path.add(course)
            for i in range(len(graph[course])):
                if not dfs(graph[course][i]):
                    return False
            
            path.remove(course)
            visted.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return  True 
        