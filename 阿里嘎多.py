import numpy as np

vec1=np.array([1,2,3,4])
print(vec1)

#创建零向量
print(np.zeros(3))
print(np.ones(4))
print(np.full(4,888 ))

print('size=',vec1.size)
print('len=',len(vec1))
print(vec1[-1])
print(type(vec1[0:3 ]))

#基本运算
vec2=np.array([5,3,6,7])
print('{}+{}={}'.format(vec1,vec2,vec1+vec2))
print('{}.dot{}={}'.format(vec1,vec2,vec1.dot(vec2)))

#求模
print(np.linalg.norm(vec1))
print(vec1/np.linalg.norm(vec1))