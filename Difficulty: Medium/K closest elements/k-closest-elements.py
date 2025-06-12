class Solution:
    def printKClosest(self, arr, k, x):
        arr=[num for num in arr if num !=x]
        arr.sort(key=lambda num: (abs(num - x),-num))
        result=arr[:k]
        return result