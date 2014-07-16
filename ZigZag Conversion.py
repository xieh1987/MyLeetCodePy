class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        length=len(s)
        aStr=''
        i=0
        while i<length:
            aStr+=s[i]
            i+=2*(nRows-1)
        for row in range(1,nRows-1):
            m=row
            while m<length:
                aStr+=s[m]
                if m+2*(nRows-1-row)<length:
                    aStr+=s[m+2*(nRows-1-row)]
                m+=2*(nRows-1)
        last=nRows-1
        while last<length:
            aStr+=s[last]
            last+=2*(nRows-1)
        return aStr
