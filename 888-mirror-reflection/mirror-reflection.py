class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p*q/gcd(p,q) #smallest distance meet
        m = lcm/p #no of times h
        n = lcm/q # v

        if m%2==0 and n%2==1: 
            return 0
        if m%2 ==1 and n%2==1:
            return 1
        if m%2 ==1 and n%2== 0:
            return 2
