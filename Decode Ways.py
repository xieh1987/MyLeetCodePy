class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        if length>=1 and s[0]!='0':
            dp[1] = 1
        for i in range(1, length):
            if (s[i-1]=='0' or s[i-1]>'2') and s[i]=='0':
                return 0
            elif s[i-1]=='0' or s[i-1]>'2' or (s[i-1]=='2' and s[i]>'6'):
                dp[i+1] = dp[i]
            elif (s[i-1]=='1' or s[i-1]=='2') and s[i]=='0':
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] = dp[i-1] + dp[i]
        return dp[length]
