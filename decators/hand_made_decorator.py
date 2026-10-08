from functools import wraps


def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} finished')
        return result
    return wrapper