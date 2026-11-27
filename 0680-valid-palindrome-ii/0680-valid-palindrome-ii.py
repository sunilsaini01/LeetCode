
class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return (self.remove(s, left + 1, right) or
                        self.remove(s, left, right - 1))

        return True

    def remove(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
