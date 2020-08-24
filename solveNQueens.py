from typing import List
from copy import deepcopy
n=4

from typing import List
from copy import deepcopy

class Solution():
    def solveNQueens(self,n):
        board = [['.' for _ in range(n)] for _ in range(n)]  #
        res=[]
        def helper(left:List,right:List,column:List):
            if len(column)==n: ####循环的结束条件
                row=[]
                for k in board:
                    row.append(' '.join(k))
                res.append(row)
            j=len(column) ####对于第j行的内容进行遍历
            for i in range(n):
                if (i in column) or (i-j in left) or (i+j in right):
                    continue
                board[j][i]='Q'
                helper(left+[i-j],right+[i+j],column+[i])
                board[j][i]='.'

        helper([],[],[])
        return res
print(n)

a=Solution()
a.solveNQueens(n)



