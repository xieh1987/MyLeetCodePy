class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend<0:
            return self.divide(-dividend, -divisor)
        res = dividend
        answer = 0
        div = abs(divisor)
        while res>=div:
            count = 1
            while res>=div:
                answer += count
                count +=count
                res -= div
                div += div
            div = abs(divisor)
        if divisor<0:
            return -answer
        else:
            return answer
