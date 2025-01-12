class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*m for i in range(n)]
        dp[0]=[1]*m
        for i in dp:
            i[0]=1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[n-1][m-1]