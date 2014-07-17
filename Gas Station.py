class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        index=0
        tankgas=0
        mingas=0
        for station  in range(len(gas)):
            if tankgas<mingas:
                index=station
                mingas=tankgas
            tankgas=tankgas+gas[station]-cost[station]
        if tankgas<0:
            return -1
        else:
            if tankgas<mingas:
                index=0
            return index
