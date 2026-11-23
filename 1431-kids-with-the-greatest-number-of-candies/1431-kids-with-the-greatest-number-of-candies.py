class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = len(candies)
        
        output = []
        total = 0
        for i in range(n):
            total = candies[i] + extraCandies
            if total >= max(candies):
                output.append(True)
            else: 
                output.append(False)
            
        return output

