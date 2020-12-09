import pytest


def add_function(a, b):
    return a + b


# @pytest.mark.parametrize("a,b,expected",[
#     (3,5,8),(-1,-2,-3),(1000,1000,2000)
# ],ids=["int","minus","bigint"])
@pytest.mark.parametrize("a", [0, 1, 2])
@pytest.mark.parametrize("b", [3, 4, 5])
def test_add(a, b):
    print("测试组合:a->%s,b->%s" % (a, b))
