from matrix import Matrix

d1=Matrix([[1,2],[3,2]])
print(d1)
print('matrix shape={}'.format(d1.shape()) )

print(Matrix.zero(2,3))

d1.T()
print('TD={}'.format(d1.T()))

I=Matrix.identity(2)
print(I)

print('d1.dot(I)={}',format(d1.dot(I)))