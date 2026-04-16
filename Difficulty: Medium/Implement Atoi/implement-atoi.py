class Solution:
    def myAtoi(self, s):
        if s=='':
            print('0')
        else:
            num=0
            sign=1
            i=0
            int_max=2**31-1
            int_min=-2**31
            while len(s)>i and s[i]==" ":
                i+=1
            if len(s)>i and (s[i]=='-' or s[i]=='+'):
                if s[i]=='-':
                    sign=-1
                i+=1
            while len(s)>i and s[i].isdigit():
                digit = int(s[i])
                if num>(int_max-digit)//10:
                    return (int_max if sign==1 else int_min)
                    break
                num = num * 10 +digit
                i+=1
            else:
                return (sign * num)