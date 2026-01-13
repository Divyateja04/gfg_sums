class Solution:
    def canServe(self, arr):
        ten = 0
        five = 0
        for i in arr:
            if i==5:
                five+=1
            if i==10:
                ten+=1
                if five>=1:
                    five-=1
                else:
                    return False
            if i==20:
                if five>=1 and ten>=1:
                    five-=1
                    ten -=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True