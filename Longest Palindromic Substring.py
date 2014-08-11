class Solution:
    # @return a string
    def longestPalindrome(self, s):
        str = '#' + '#'.join(s) + '#'
        p, center, mx = [0]*len(str), 0, 0
        
        for i in range(len(str)):
            if mx > i:
                p[i] = min(p[2*center-i], mx-i)
                
            while i-p[i]-1>=0 and i+p[i]+1<len(str) and str[i+p[i]+1]==str[i-p[i]-1]:
                p[i] += 1
                
            if i+p[i]>mx:
                center = i
                mx = i + p[i]
                
        pos = p.index(max(p))
        subStr = str[pos-p[pos]:pos+p[pos]+1]
        return subStr.replace('#', '')
