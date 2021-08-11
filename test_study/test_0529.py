#!/usr/bin/python3
# @Time    : 2021/5/29 1:30 下午
# @Author  : WangXin
a,b=1,2
class Test():

    def __init__(self):
        c=1.1
        print(c)
        self.c = 5

    def test_add(self):
        c = a+b
        print(c)

    def test_jianfa(self):
        c = b-a
        print(c)

    def test_c(self):
        print(self.c)

if __name__=='__main__':
    t = Test()
    t.test_add()
    t.test_jianfa()
    t.test_c()

