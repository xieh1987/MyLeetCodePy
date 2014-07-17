class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candylist=[1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                candylist[i+1]=candylist[i]+1
        sum=candylist[len(ratings)-1]
        for j in range(len(ratings)-1,0,-1):
            if ratings[j-1]>ratings[j] and candylist[j-1]<=candylist[j]:
                candylist[j-1]=candylist[j]+1
            sum=sum+candylist[j-1]
        return sum
