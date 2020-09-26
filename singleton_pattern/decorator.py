import functools


def singleton(class_):

    @functools.wraps(class_)
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton._instance is None:
            wrapper_singleton._instance = class_(*args, **kwargs)
        return wrapper_singleton._instance
    wrapper_singleton._instance = None
    return wrapper_singleton

