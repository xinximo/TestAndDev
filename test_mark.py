import pytest


class Test_demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 1
        b = 2
        assert a + b == 3
        print("我的第一个用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_one(self):
        a = 3
        b = 3
        assert a * b == 9
        print("我的第二个用例")
