import functools
import time


def my_dec(func):
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        print('Проверка запущена...')
        kwargs['start_time'] = time.time()
        return func(*args, **kwargs)
    return wrap_func
