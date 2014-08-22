class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if needle=='':
            return haystack
        lengthH, lengthN = len(haystack), len(needle)
        for i in range(lengthH-lengthN+1):
            if haystack[i:i+len(needle)]==needle:
                return haystack[i:]
        return None
