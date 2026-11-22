class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        output = []
        total = 0
        for i in range(n):
            total += nums[i]
            output.append(total)
        return output
        