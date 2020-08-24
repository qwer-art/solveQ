n=4

def solveQ(n):
    board=[['.']*n for _ in range(n)]
    res=[]
    def solveQ(left,right,colunm):
        if len(colunm)==n:
            tmp=[]
            for k in board:
                tmp.append(''.join(k))
            res.append(tmp)

