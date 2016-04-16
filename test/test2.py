#!/usr/bin/env python3
# coding=utf-8

class A(object):
    def __init__(self):
        self.a1 = 2.0
        self.a2 = 3.0
        print("this is A")
    def set_a(self, val1, val2):
        self.a1 = val1
        self.a2 = val2
class B(object):
    def __init__(self):
        print("this is B")
    def tp(self):
        print("success B fun")
        
class C(B):
    def __init__(self):
        super(C, self).__init__()
        self.data = A()
    def set_val(self):
        print(self.data.a1, self.data.a2)
        self.data.set_a(4.0,5.0)
        print(self.data.a1, self.data.a2)
        self.tp()

test = C();
test.set_val()
