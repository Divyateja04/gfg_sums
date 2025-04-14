#User function Template for python3
class Solution:
    def findOrder(words):
        # code here
        from collections import defaultdict
        adj=defaultdict(set)
        ino=defaultdict(int)
        lth=len(words)
        for i in range(lth-1):
            for k in range(i+1,lth):
                j=0
                mx=min(len(words[i]),len(words[k]))
                while j<mx and words[i][j]==words[k][j]:
                    j+=1
                if j<mx:
                    if words[k][j] not in adj[words[i][j]]:
                        ino[words[k][j]]+=1
                        adj[words[i][j]].add(words[k][j])
                else:
                    if mx==len(words[k]) and mx<len(words[i]):
                        return ""
        st=set()
        for w in words:
            st.update(list(w))
        ret=[]
        q=[x for x in st if ino[x]==0]
        while q:
            cur=q.pop()
            ret.append(cur)
            for nxt in adj[cur]:
                ino[nxt]-=1
                if ino[nxt]==0:
                    q.append(nxt)
        if len(ret)<len(st):
            return ""
        return ''.join(ret)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
from collections import deque

#Position this line where user code will be pasted.


def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends