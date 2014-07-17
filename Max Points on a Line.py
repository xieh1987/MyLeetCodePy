# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        maxNum=0
        for i in range(len(points)):
            map, same, inf, maxCurr, start={}, 1, 0, 0, points[i]
            for j in range(i+1,len(points)):
                end=points[j]
                if start.x==end.x and start.y==end.y:
                    same+=1
                elif start.x==end.x:
                    inf+=1
                else:
                    slope=float(end.y-start.y)/(end.x-start.x)
                    if slope not in map:
                        map[slope]=1
                    else:
                        map[slope]+=1
            for slope in map:
                maxCurr=max(map[slope]+same, maxCurr)
            maxNum=max(maxNum, inf+same, maxCurr)
        return maxNum
