class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        pre = strs[0]
        for i in range(len(strs[0])):
            for str in strs:
                if i>=len(str) or strs[0][i]!=str[i]:
                    pre = pre[:i]
        return pre
