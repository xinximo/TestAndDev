#!/usr/bin/python3
# @Time    : 2021/7/22 16:22
# @Author  : Wangx
import datetime
import time
import logging
from logging import handlers


class TimeStamp:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename='app.log', level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        """
        实例化TimedRotatingFileHandler
        interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        S 秒
        M 分
        H 小时、
        D 天、
        W 每星期（interval==0时代表星期一）
        midnight 每天凌晨
        """
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)

    def datetime_to_sec_timestamp(self, _data_time: str):
        try:
            _time_stamp = int(time.mktime(time.strptime(_data_time, "%Y-%m-%d %H:%M:%S")))
            print(f"{_data_time}转秒级时间戳：", _time_stamp)
        except Exception as e:
            self.logger.error(e)
            print(f"格式不对，请输入格式例如：2021-07-22 00:00:00")

    def datetime_to_msec_timestamp(self, _data_time: str):
        try:
            _time_stamp = int(time.mktime(time.strptime(_data_time, "%Y-%m-%d %H:%M:%S")) * 1000)
            print(f"{_data_time}转毫秒级时间戳：", _time_stamp)
        except Exception as e:
            self.logger.error(e)
            print(f"格式不对，请输入格式例如：2021-07-22 00:00:00")

    def sec_timestamp_to_datetime(self, _time_stamp: str):
        try:
            _data_time = datetime.datetime.fromtimestamp(float(_time_stamp))
            print('秒级时间戳转日期:', _data_time.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            self.logger.error(e)
            print(f"格式不对，请输入10位格式例如：1626946200")

    def msec_timestamp_to_datetime(self, _time_stamp: str):
        try:
            _data_time = datetime.datetime.fromtimestamp(float(_time_stamp) / 1000)
            print('毫秒级时间戳转日期:', _data_time.strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            self.logger.error(e)
            print(f"格式不对，请输入13位格式例如：1626946200000")

    def now_sec_timestamp(self):
        print("当前时间秒级时间戳：", int(time.time()))

    def now_msec_timestamp(self):
        print("当前时间毫秒级时间戳：", int(round(time.time() * 1000)))


if __name__ == "__main__":
    t = TimeStamp()
    while True:
        time_type = input("请输入你要做的选项：\n"
                          "如需年月日时分秒转换秒级时间戳，请输入：1\n"
                          "如需年月日时分秒转换毫秒级时间戳，请输入：2\n"
                          "如需秒级时间戳转换日期，请输入：3\n"
                          "如需毫秒级时间戳转换日期，请输入：4\n"
                          "如需当前时间秒级时间戳，请输入：5\n"
                          "如需当前时间毫秒级时间戳，请输入：6\n")
        if time_type == "1":
            _sec_date_time = input("请输入需要转换的年月日时分秒（格式：2021-07-22 00:00:00）：")
            t.datetime_to_sec_timestamp(_sec_date_time)
        elif time_type == "2":
            _msec_date_time = input("请输入需要转换的年月日时分秒（格式：2021-07-22 00:00:00）：")
            t.datetime_to_msec_timestamp(_msec_date_time)
        elif time_type == "3":
            _sec_timestamp = input("请输入秒级时间戳（格式10位：1626946200）：")
            t.sec_timestamp_to_datetime(_sec_timestamp)
        elif time_type == "4":
            _msec_timestamp = input("请输入毫秒级时间戳（格式13位：1626946200000）：")
            t.msec_timestamp_to_datetime(_msec_timestamp)
        elif time_type == "5":
            t.now_sec_timestamp()
        elif time_type == "6":
            t.now_msec_timestamp()
        else:
            print("您输入了不存在的编号，请重新输入：")
