class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        step, num = len(L[0]), len(L)
        result = []
        for i in range(len(S)-step*num+1):
            aList = [S[j:j+step] for j in range(i, i+step*num, step)]
            found = True
            for word in L:
                if word in aList:
                    aList.remove(word)
                else:
                    found = False
                    break
            if found:
                result.append(i)
        return result
