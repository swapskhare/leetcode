class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(curr, path):
            if curr == target:
                results.append(list(path))
                return
            for n in graph[curr]:
                path.append(n)
                backtrack(n, path)
                path.pop()

        path = [0]
        backtrack(0, path)

        return results