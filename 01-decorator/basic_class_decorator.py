# coding:utf-8

class logging:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[DEBUG]: enter function {func}()'.format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)

@logging
def say(something):
    print('hello {}!'.format(something))

@logging
def do(something):
    print('do {}!'.format(something))

if __name__ == '__main__':
    say('Bob')
    do('Dunk')
