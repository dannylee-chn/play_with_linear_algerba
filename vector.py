import math
EPSILON=1e-8

class Vector:

    def __init__(self,lst):
        self._values =lst

    def __len__(self):
       return len(self._values)

    def __setitem__(self, index, value):
        self._values[index] = value

    def __getitem__(self,index):
        return self._values[index]

    def __repr__(self):
        return 'Vector({})'.format(self._values)

    def __str__(self):
        return '({})'.format(','.join(str(e) for e in self._values))


    #向量加法
    def __add__(self,another):
        assert len(self) == len(another), \
            'error is adding.lengths of vector must be same'
        return Vector([a+b for a,b in zip(self,another)])

    def __sub__(self,another):
        assert len(self) == len(another), \
            'error is substracting.lengths of vector must be same'
        return Vector([a-b for a,b in zip(self,another)])

   #顺序重要
    def __mul__(self,k):
        return Vector([a*k for a in self._values])

    def _pos__(self):
        return 1*self

    def __neg__(self):
        return -1*self

    @classmethod
    def zero(cls,dim):
        return cls([0]*dim)


#向量的大小-模，向量的方向-单位向量（归一化，规范化）

    def norm(self):
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        if self.norm()<EPSILON:
           raise ValueError('Normalize error!norm is zero.')
        return Vector([e/self.norm() for e in self])

#向量的点乘:先将两个向量统一到一个方向上再做乘法---cos:判断相似度 （推荐系统）
    def dot(self,another):
         assert len(self)==len(another),\
                ('error in dot product.lengths of vector must be same')

         return sum( a*b for a,b in zip(self,another) )


