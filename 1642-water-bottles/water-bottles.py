class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sumb = numBottles
        x = numBottles
        while True:
            y = x//numExchange
            z = x%numExchange
            sumb+=y
            x = y+z
            if(x<numExchange):
                break

        return sumb
