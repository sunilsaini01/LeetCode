class Solution(object):
    def maximumWealth(self, accounts):
        m = len(accounts)
        n = len(accounts[0])
        max_wealth = 0
        for i in range(m):
            total = 0
            for j in range(n):
                total += accounts[i][j]
            max_wealth = max(max_wealth , total)
        return max_wealth

        