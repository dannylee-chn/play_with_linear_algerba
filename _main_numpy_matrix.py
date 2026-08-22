import numpy as np

if __name__=='__main__':

    #矩阵的创建
    A=np.array([[1,2,3],[4,5,6],[7,8,9]])
    
    #矩阵的属性
    print(A.shape)
    print(A.T)

    #获取矩阵中的元素(默认行）
    print(A[1,2])
    print(A[2])
    print(A[ :,2])

    #矩阵的基本运算
    B=np.array([[5,6,7],[8,9,10],[11,12,14]])
    print(A+B)
    print(A-B)
    print(10*A)
    print(A.dot(B))

    c=np.array([3,9,80])
    print(A.dot(c))

    #单位矩阵
    I=np.identity(3)
    print(I)
    print(A.dot(I))

    #逆矩阵
    invA=np.linalg.inv(A)
    print(invA)
    print('a='.format(A.dot(invA)))
    print(invA.dot(A))