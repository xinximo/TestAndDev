import pytest


class Test_demo2():
    def test_one2(self, myfixture):
        print("执行test_one")
        assert 1 + 1 == 2

    def test_two2(self, myfixture):
        print("执行test_two")
        assert 1 + 1 == 2

    def test_three2(self):
        print("执行test_three")
        assert 1 + 1 == 2
