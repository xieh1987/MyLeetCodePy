class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        DP = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        DP[0][0] = True
        for k in range(1, len(p)+1):
            if p[k-1]=='*' and k>=2:
                DP[0][k] = DP[0][k-2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1]=='.':
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1]=='*':
                    DP[i][j] = DP[i][j-1] or DP[i][j-2] or (DP[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    DP[i][j] = DP[i-1][j-1] and s[i-1]==p[j-1]
        return DP[len(s)][len(p)]
