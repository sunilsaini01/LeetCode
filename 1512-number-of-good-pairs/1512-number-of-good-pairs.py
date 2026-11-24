class Solution(object):
    def numIdenticalPairs(self, nums):
        i = 0
        total = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    total = total + 1

        return total 
        