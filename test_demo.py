import allure
import pytest

# def add_function(a, b):
#     return a + b
#
#
# # @pytest.mark.parametrize("a,b,expected",[
# #     (3,5,8),(-1,-2,-3),(1000,1000,2000)
# # ],ids=["int","minus","bigint"])
# @pytest.mark.parametrize("a", [0, 1, 2])
# @pytest.mark.parametrize("b", [3, 4, 5])
# def test_add(a, b):
#     print("测试组合:a->%s,b->%s" % (a, b))
import yaml


@allure.feature("测试类")  # pytest test_demo.py --allure-features="测试类" --alluredir=./report1 -clean
class TestDemo:
    @allure.severity(allure.severity_level.NORMAL)  # pytest test_demo.py --allure-severities="normal"
    @allure.story("环境区分")
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_yaml(self, env):
        if "test" in env:
            print("测试环境为:", env["test"])
        elif "dev" in env:
            print("开发环境为:", env["dev"])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("展示路径")
    def test_show(self):
        with allure.step("步骤1:输出路径"):
            print(yaml.safe_load(open("./env.yml")))
        with allure.step("步骤2:输出文字"):
            assert 1 + 2 == 3
            print("这是一条文字测试用例")

    path = "http://www.baidu.com"

    @allure.title("打开百度")
    @allure.testcase(path, "测试链接")
    def test_with_testcase_link(self):
        pass

    def test_attach_text(self):
        allure.attach("这是一个测试文本:", attachment_type=allure.attachment_type.TEXT)

    def test_attach_html(self):
        allure.attach("这是一个测试html:", "HTML名称", attachment_type=allure.attachment_type.HTML)

    def test_attach_photo(self):
        allure.attach.file("E:/QQ截图20190730143014.png", name="图片名称", attachment_type=allure.attachment_type.PNG)
# allure serve ./report1调用allure生成报告
