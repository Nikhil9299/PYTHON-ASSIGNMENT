s=lambda x,y:x+y
print(s(4,5))

#map
n=[2,3,4,5,6,7,8]
square=list(map(lambda x:x*x,n))
print(square)

#filter
n=[1,2,3,4,5,6,7,8,9]
def is_grt_5(n):
    return n>5
grt_thn_5=list(filter(is_grt_5,n))
print(grt_thn_5)

#reduce - adding or multiplyng or divide al other stuff with the adjustng num or side num
#reduce(fun, seq) takes function as 1st and sequence as 2nd argument
from functools import reduce
a=[1,2,3,4,5]
s=reduce(lambda x,y:x*y,a)
print(s)

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)
