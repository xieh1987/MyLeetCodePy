class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry=1
        for digit in range(len(digits)):
            temp=digits[-1-digit]+carry
            digits[-1-digit]=temp%10
            carry=temp//10
        if carry:
            digits.insert(0,carry)
        return digits
