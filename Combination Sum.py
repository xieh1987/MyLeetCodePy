class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        dp = {}; dp[0] = [[]]
        for i in range(1, target+1):
            dp[i] = []
            for num in candidates:
                if num<=i:
                    for alist in dp[i-num]:
                        tmp = sorted(alist+[num])
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
        return dp[target] if dp[target] else []
