class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish  = 0

        while q:
            node = q.popleft()
            finish += 1
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return finish == numCourses