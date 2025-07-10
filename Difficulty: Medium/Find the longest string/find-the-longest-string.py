class Solution():
    def longestString(self, arr):
        dic = {}
        ans = ''
        for i in arr:
            dic[i]=1
        n = len(arr)
        for i in arr:
            s= ''
            l = len(i)
            for j in i:
                s+=j
                if dic.get(s,0)==0:
                    l=0
                    break
            l_ans =len(ans)
            if l_ans<=l: 
                if l_ans == l:
                    ans = min (ans,i)
                else:
                    ans = i
        return ans 
        