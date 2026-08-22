import vector
from vector import Vector

d1=Vector([1,2,3])
print(d1)
print(repr(d1))
print(len(d1) )
print(d1[0])
print(d1[1])
print(d1[2])


print('{}*{}={}'.format(d1,3,d1*3))

#print('-{}={}'.format(d2,-d2))
zero1=Vector.zero(2)
print(zero1)

d2=Vector([0,0,0])
# print('normalize {} is {}'.format(d2,d2.normalize()))

d3=Vector([6,4,2])

print(d1.dot(d3))