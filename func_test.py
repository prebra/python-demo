# var1 = 1
# def test(a, *b):
#     global var1
#     var1 = 2
#     print(var1)
#
# test(1)
# print(var1)
#
# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))


# for i in range(10, 20, 2):
#     print(i)

# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x = x + step
#
#
# for i in frange(10, 20, 0.5):
#     print(i)

# lambda
# def add(x,y):
#     return x+y
#
# lambda x,y: x+y
#
# lambda x:x<= (month,day)
# def func1(x):
#     return x<= (month,day)
#
# lambda  item:item[1]
# def func2(item):
#     return item[1]

# list1 = [1, 2, 3, 4]
# print(list(filter(lambda x: x > 2, list1)))
#
# list2 = [5, 6, 7, 8]
# print(list(map(lambda x,y: x+y, list1, list2)))
#
# from functools import reduce
# reduce(lambda x,y: x+y, [2,3,4],1)
#
# for i in zip(list1, list2):
#     print(i)
#
# dicta = {'a': 'aa', 'b': 'bb'}
# print(dict(zip(dicta.values(), dicta.keys())))

# 闭包
# def counter(first=0):
#     cnt = [first]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
#
# num1 = counter(5)
# print(num1())
# print(num1())
# print(num1())

# def a_line(a, b):
#     def arg_y(x):
#         return a*x+b
#     return arg_y

def a_line(a, b):
    return lambda x: a * x + b


line1 = a_line(3, 5)
print(line1(10))
print(line1(20))
