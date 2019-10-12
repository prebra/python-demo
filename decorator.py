# 装饰器

import time
print(time.time())


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间是 %s 秒' % (stop_time - start_time))
    return wrapper


@timmer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()

# 带参数


def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')
        return nei
    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('sub_module')
def sub(a, b):
    print(a - b)


add(1, 2)
sub(4, 3)
