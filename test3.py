from functools import reduce

a = reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])
print(a)
b = map(lambda x: x * 3, [1, 2, 4, 8])
print(list(b))
c = lambda x, y: x if x < y else y
print(c(1, 2))
def he(func):
    def wrapper(*args, **kwargs):
      print('he')
      return func(*args, **kwargs)
    return wrapper
@he
def hc(a, b, c):
    print(a + b + c)
    print('hc')

@he
def h(a, b):
    print(a+b)
hc(1, 2, 3)
h(1, 2)