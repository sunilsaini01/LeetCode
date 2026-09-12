class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        for i in range(len(nums)):

            if nums[i] == max or nums[i] == second_max or nums[i] == third_max:
                continue 

            if nums[i] > max:
                third_max = second_max
                second_max = max
                max = nums[i]
            
            elif nums[i] > second_max and nums[i]!= max:
                third_max = second_max
                second_max = nums[i]

            elif nums[i]>third_max:
                third_max = nums[i]

        if third_max == float('-inf'):
            return max 

        return third_max



          