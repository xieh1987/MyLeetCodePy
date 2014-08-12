class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits)==0:
            return ['']
        aDict = {'1':[''], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z'], '0':['']}
        result = []
        aList = list(digits)
        self.helper(result, '', aList, aDict)
        return result
        
    def helper(self, result, currStr, aList, aDict):
        length = len(aList)
        if length==1:
            for char in range(len(aDict[aList[0]])):
                result.append(currStr+aDict[aList[0]][char])
        else:
            num = aList[0]
            for char in range(len(aDict[num])):
                self.helper(result, currStr+aDict[num][char], aList[1:], aDict)
