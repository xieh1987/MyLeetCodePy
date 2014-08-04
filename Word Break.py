class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        possible=[]
        for i in range(len(s)):
            if s[0:i+1] in dict:
                possible.append(True)
            else:
                found = False
                for j in range(i):
                    if possible[j]==True and s[j+1:i+1] in dict:
                        found = True
                        break
                possible.append(found)
        return possible[-1]
