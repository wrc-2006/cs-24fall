class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp=[[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                dp[i][j]=True
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
        ans=''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i][j] and j-i+1>len(ans):
                    ans=s[i:j+1]
        return ans

if __name__=="__main__":
    sol=Solution()
    print(sol.longestPalindrome(input()))
        
