class Solution:
    # @return a string
    def intToRoman(self, num):
        romanDict={1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        keyList, length, numRoman = sorted(romanDict.keys()), len(romanDict), ''
        for i in reversed(range(length)):
            key = keyList[i]
            while num>=key:
                numRoman += romanDict[key]
                num -= key
        return numRoman
