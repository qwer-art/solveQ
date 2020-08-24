from typing import List
S='mii'
class Solution:
    def permutation(self, S: str) -> List[str]:
        n=len(S)
        if n==0:
            return [""]
        res=[]
        for i in range(n):
            if S[i] in S[:i]:   #只需判断S[i]是否在S[:i]中出现过即可
                continue
            for s1 in self.permutation(S[:i]+S[i+1:]):
                res.append(S[i]+s1)
        return res

a=Solution()
print(a.permutation(S))
