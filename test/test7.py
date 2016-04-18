#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    使用装饰器
'''
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)

def end(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("Call %s"%func.__name__)
        return func(*args, **kw)
    return wrapper

@end
def test(a):
    print("20160418{0}".format(a))
test("test")
