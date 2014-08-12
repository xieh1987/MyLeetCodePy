class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        aDict, result = {}, []
        num.sort()
        
        for m in range(len(num)):
            for n in range(m+1, len(num)):
                if num[m]+num[n] not in aDict:
                    aDict[num[m]+num[n]]=[(m,n)]
                else:
                    aDict[num[m]+num[n]].append((m,n))
                    
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                tf = target - num[i] - num[j]
                if tf in aDict:
                    for k in aDict[tf]:
                        if k[0]>j and [num[i], num[j], num[k[0]], num[k[1]]] not in result:
                            result.append([num[i], num[j], num[k[0]], num[k[1]]])
            
        return result
