# coding: utf-8

def debug(func):
    def wrapper(something):  # 指定一模一样的参数
        print('[DEBUG]: enter {}()'.format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数

@debug
def say(something):
    print('hello {}!'.format(something))

@debug
def do(something):
    print('do {}!'.format(something))

if __name__ == '__main__':
    say('Bob')
    do('Dunk')
