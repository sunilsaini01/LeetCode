class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        while x != 0:
            digit = int(x%10)

            if rev > 2147483647  // 10:
                return 0
                 
            rev = rev * 10 + digit
            x = int(x//10)

        return sign * rev