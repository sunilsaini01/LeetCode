class Solution(object):
    def shuffle(self, nums, n):
        
        left = 0
        right = n
        output = []
        for i in range(n):
            output.append(nums[left])
            output.append(nums[right])
            left += 1
            right += 1

        return output

            

        