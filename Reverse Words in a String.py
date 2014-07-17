class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, str):
        alist = str.split(" ")
        anotherlist = []
        for word in alist:
            if word!=" ":
                anotherlist.append(word)
        astring = ""
        while len(anotherlist) > 0:
            tempstr=anotherlist.pop()
            if tempstr!="":
                astring=astring+tempstr+" "
        astring=astring[:len(astring)-1]
        return astring
