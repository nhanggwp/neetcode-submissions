class Solution:
   def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:
            graph = {i : [] for i in range(numCourses)}

            for a,b in prerequisites:
                graph[b].append(a)
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

        if(not canFinish(numCourses,prerequisites)):
            return []
        
        graph = {i : [] for i in range(numCourses)}
        
        for a,b in prerequisites:
                graph[b].append(a)

        path = []
        vistied = set()
        def dfs(x):
            if x in vistied:
                return
            for i in graph[x]:
                dfs(i)
            path.append(x)
            vistied.add(x)
            return
        
        for i in range(numCourses):
            dfs(i)
        
        return path[::-1]