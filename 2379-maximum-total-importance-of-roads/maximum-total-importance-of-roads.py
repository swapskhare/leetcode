class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = [0]*n
        cost = 1
        ans = 0
        for a,b in roads:
            connections[a] += 1
            connections[b] += 1
        
        connections.sort()

        for conn in connections:
            ans += conn * cost
            cost += 1
        return ans
        
