class Solution:
    def removeSpaces(self, s):
        a = []
        for i in s:
            if i != ' ':
                a.append(i)
        return "".join(a)