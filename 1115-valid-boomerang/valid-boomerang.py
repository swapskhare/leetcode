class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1,y1),(x2,y2),(x3,y3) = points

        area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
        
        if area !=0:
            return True
        else:
            return False
        