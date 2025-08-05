import re
class Solution:
	def isPalinSent(self, s):
	    res=""
	    for i in s:
	        if i.isalnum():
	            res=res+i
	    res=res.lower()
	    if res == res[::-1]:
	        return True
	    return False