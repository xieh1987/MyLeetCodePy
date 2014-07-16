class Solution:
    # @return a boolean
    def isValid(self, s):
        aList=[]
        valid=True
        map={'(':')','[':']','{':'}'}
        for i in range(len(s)):
            if s[i] in map:
                aList.append(s[i])
            else:
                if aList!=[]:
                    valid=(map[aList.pop()]==s[i])
                    if not valid:
                        break
                else:
                    valid=False
        return (valid and aList==[])
