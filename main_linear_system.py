from LinearSystem import inv

from vector import Vector
from matrix import Matrix

if __name__=='__main__':

    A=Matrix([[1,2],[3,4]])
    inv(A)
    print(inv(A))
