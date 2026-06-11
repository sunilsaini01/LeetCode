class Solution(object):
    def reverse(self, x):
        """

        :type x: int

        :rtype: int

        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        num = 0

        while x:

            digit = x % 10
            num = num * 10 + digit
            x = x // 10

        num = num *sign

        if num < -2**31 or num > 2**31 - 1:
            return 0

        return num