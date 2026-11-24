class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        left = 0
        right = 0

        while left < len(s) and right < len(t):

            if s[left] != t[right]:
                return False

            left += 1
            right += 1

        return True
        