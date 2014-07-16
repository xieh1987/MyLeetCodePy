class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map={}
        for i in range(len(num)):
            val=target-num[i]
            if val in map:
                return(map[val]+1, i+1)
            map[num[i]]=i
            
