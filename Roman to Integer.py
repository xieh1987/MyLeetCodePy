class Solution:
    # @return an integer
    def romanToInt(self, s):
        romanDict={'I':1, 'V':5,  'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in reversed(range(len(s))):
            if i==len(s)-1:
                num += romanDict[s[i]]
            else:
                if romanDict[s[i]]>=romanDict[s[i+1]]:
                    num += romanDict[s[i]]
                else:
                    num -= romanDict[s[i]]
        return num
