class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        prereq = { c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            prereq[crs].append(pre)


        output = []

        visit, cycle = set(), set()

        def dfs(crs):
            #check if cycle is present
            if crs in cycle:
                return False
            if crs in visit:
                return True

            #add crs to cycle 
            cycle.add(crs)
            #checl if cycle formed in any iteration of crs
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            # remove from cycle, add to visited as no cycle found, add to output
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return output