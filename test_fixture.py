import pytest


class Test_demo():
    def test_one(self):
        print("执行test_one")
        assert 1 + 1 == 2

    def test_two(self, myfixture):
        print("执行test_two")
        myenv = myfixture
        print(f"---testtwo in {myenv}")
        assert 1 + 1 == 2

    @pytest.mark.run(order=1)
    def test_three(self):
        print("执行test_three")
        pytest.assume(1 + 1 == 2)
        pytest.assume(1 + 2 == 3)
        pytest.assume(1 + 3 == 4)
