import pytest
from pythoncode.calculator import Caculator


class TestCalc:
    def setup_class(self):
        self.calc = Caculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 200, 300)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 2), (6, 2, 4), (300, 200, 100)
    ], ids=["int1", "minus1", "bigint1"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 3, 15), (6, 2, 12), (300, 200, 60000)
    ], ids=["int2", "minus2", "bigint2"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (6, 3, 2), (6, 2, 3), (300, 100, 3)
    ], ids=["int3", "minus3", "bigint3"])
    def test_chu(self, a, b, expect):
        assert expect == self.calc.chu(a, b)
