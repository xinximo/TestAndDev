import pytest
import yaml


def get_data(path, key):
    with open(path) as f:
        datas = yaml.safe_load(f)
        # print(datas[key])
        return datas[key]
        # add_datas = datas["adddatas"]
        # sub_datas = datas["subdatas"]
        # mul_datas = datas["muldatas"]
        # div_datas = datas["divdatas"]
        # all_ids = datas["myid"]
        # return [add_datas, sub_datas, mul_datas, div_datas, all_ids]

class TestCalc:
    path = "./calc_data.yml"

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_data(path, "adddatas"), ids=get_data(path, "myid"))
    def test_add(self, a, b, expect, start_calc):
        assert expect == start_calc.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data(path, "subdatas"), ids=get_data(path, "myid"))
    def test_sub(self, a, b, expect, start_calc):
        assert expect == start_calc.sub(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_data(path, "muldatas"), ids=get_data(path, "myid"))
    def test_mul(self, a, b, expect, start_calc):
        assert expect == start_calc.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_data(path, "divdatas"), ids=get_data(path, "myid"))
    def test_div(self, a, b, expect, start_calc):
        try:
            assert expect == start_calc.div(a, b)
        except:
            print("参数有误")
# class TestCalc:
#
#     @pytest.mark.run(order=1)
#     @pytest.mark.parametrize("a,b,expect", get_data()[0], ids=get_data()[4])
#     def test_add(self, a, b, expect, start_calc):
#         assert expect == start_calc.add(a, b)
#
#     @pytest.mark.run(order=2)
#     @pytest.mark.parametrize("a,b,expect", get_data()[1], ids=get_data()[4])
#     def test_sub(self, a, b, expect, start_calc):
#         assert expect == start_calc.sub(a, b)
#
#     @pytest.mark.run(order=3)
#     @pytest.mark.parametrize("a,b,expect", get_data()[2], ids=get_data()[4])
#     def test_mul(self, a, b, expect, start_calc):
#         assert expect == start_calc.mul(a, b)
#
#     @pytest.mark.run(order=4)
#     @pytest.mark.parametrize("a,b,expect", get_data()[3], ids=get_data()[4])
#     def test_div(self, a, b, expect, start_calc):
#         try:
#             assert expect == start_calc.div(a, b)
#         except:
#             print("参数有误")
