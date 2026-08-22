from matrix import Matrix
from vector import Vector
import numpy as np
from _global import is_zero
class LinearSystem:

    def __init__(self,A,b):

          #assert A.row_num()==len(b),'row A must be equal to len b'
          self._m=A.row_num()
          self._n=A.col_num()


          ##assert self._m==self._n  ## TODO:no this restriction
          self.pivots=[]

          if isinstance(b,Vector):
              row_list = [np.hstack([A.row_vector(i), b[i]]) for i in range(self._m)]
              self.Ab = Vector(np.array(row_list))
          if isinstance(b,Matrix):
              row_list = [np.hstack([A.row_vector(i), b.row_vector(i)]) for i in range(self._m)]
              self.Ab = Vector(np.array(row_list))


    def max_row(self,index_i,index_j,n):

        best,ret=self.Ab[index_i][index_j],index_i
        for i in range(index_i+1,n):
            if self.Ab[i][index_j]>best:
                best,ret=self.Ab[i][index_j],i
        return ret


    def _forward(self):
        #n=self._m
        i,k=0,0
        #for i in range(n):
        while i<self._m and k<self._n:
            #看Ab[i][k]是否可以是主元 
            max_row=self.max_row(i,k, self._m)
            self.Ab[i],self.Ab[max_row]=self.Ab[max_row],self.Ab[i]

            if is_zero(self.Ab [i][k]):
                k+=1
            else:
                self.Ab[i]=self.Ab[i] / self.Ab[i][k]    ##TODO:self.Ab[i][i]==0
            for j in range(i+1,self._m):
                self.Ab[j]=self.Ab[j]-self.Ab[j][k]*self.Ab[i]
                self.pivots.append(k)
                i+=1

    def _backward(self):

        n=len(self.pivots)
        for i in range(n-1,-1,-1):
            k=self.pivots[i]
            for j in range(i-1,-1,-1):
                self.Ab[j]=self.Ab[j]-self.Ab[j][k]*self.Ab[i]


    def gauss_jordan_elimination(self):

        self._forward()
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(''.join(str(self.Ab[i][j])for j in range(self._n)),end='')
            print('|',self.Ab[i][-1])

def inv(A):

    if A.row_num()!=A.col_num():
        return None

    n=A.row_num()
    ls=LinearSystem(A,Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None

    invA=[[ row[i] for i in range(n,2*n)]for row in ls.Ab]
    return Matrix(invA)