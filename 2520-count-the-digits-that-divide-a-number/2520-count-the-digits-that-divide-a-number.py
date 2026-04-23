class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in str(num):
            val = int(i)
            if num % val == 0:
                count += 1
        return count 

