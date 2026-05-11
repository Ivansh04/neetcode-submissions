class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        
        for i in range(n):
            hs={}
            hs1={}
            for j in range(n):
                if board[i][j] in hs and board[i][j]!='.':
                    return False
                hs[board[i][j]]=hs.get(board[i][j],0)+1 

                if board[j][i] in hs1 and board[j][i]!='.':
                    return False
                hs1[board[j][i]]=hs1.get(board[j][i],0)+1 

        a,b=0,3
        for e in range(3):
           c,d=0,3
           for f in range(3):   
                hs={}
                for i in range(a,b):
                   
                   for j in range(c,d):
                      if board[i][j] in hs and board[i][j]!='.':
                         return False
                      hs[board[i][j]]=hs.get(board[i][j],0)+1
                c+=3
                d+=3
           a+=3
           b+=3
        return True
                

        
            



        