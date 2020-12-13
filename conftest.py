import pytest
from pythoncode.calculator import Caculator
import yaml


@pytest.fixture(params=["***参数1***", "***参数2***"])
def myfixture(request):
    print(f"执行我的fixture,里面的参数是{request.param}")
    yield request.param  # 类似return且执行下面语句
    print("清理数据等操作,激活fixture里面的teardown操作")


@pytest.fixture(scope="module")
def start_calc():
    calc = Caculator()
    print("开始计算")
    return calc


def pytest_collection_modifyitems(session, config, items):
    print(type(items))  # items是一个列表
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    # if "add" in item._nodeid:
    #     item.add_marker(pytest.mark.add)
    # if "div" in item._nodeid:
    #     item.add_marker(pytest.mark.div)
