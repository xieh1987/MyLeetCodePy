class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        tail=0
        maxNum=0
        subStr=''
        for head in range(len(s)):
            if s[head] not in subStr:
                subStr+=s[head]
            else:
                maxNum=max(maxNum, len(subStr))
                while s[tail]!=s[head]:
                    tail+=1
                tail+=1
                subStr=s[tail:head+1]
        return max(maxNum, len(subStr))
