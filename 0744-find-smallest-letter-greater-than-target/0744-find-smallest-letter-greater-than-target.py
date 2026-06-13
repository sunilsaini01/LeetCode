class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0
        high = len(letters) - 1
        ans = letters[0]

        while low <= high:

            mid = (low + high) // 2

            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ans