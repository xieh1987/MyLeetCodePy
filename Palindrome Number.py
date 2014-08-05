class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        new, copy=0, x
        while copy:
            new=new*10+copy%10
            copy//=10
        return x==new
