"""
一个类文件实现一个功能：抓取 http://www.jzzs.com.cn/ 网站的效果图
"""
import os
import shutil
import sys
from urllib import request
import re

from print_custom import print_list


class SpiderToday():
    """
    类概述：
    1 入口方法为：go 方法，只需实例化类并调用入口方法即可实现功能
    2 抓取步骤：
        1 url_base (str)：http://www.jzzs.com.cn/shijing/p/1，后面的1为可变页码，需要循环处理
        2 url_all (list)：循环处理 url_base，获得所有页面的地址，存入 url_all 中
        3 循环抓取 url_all 的每个地址
            3.1 根据地址抓取页面内容
            3.2 正则表达式寻找内容，获得 title 和 image 地址
            3.3 新建文件夹并下载对应的文件到指定的文件夹中
    """
    url_all = []
    pattern_top = 'content_photo_title_01"><a href="/case/([\s\S]*?)</a>'

    @staticmethod
    def __get_url_base():
        """
        获取所有效果图页面的母页面的地址
        :return: 返回包含所有效果图页面的母页面的地址的列表
        """

        temp = 'http://www.jzzs.com.cn/shijing/p/'
        result = [temp + str(x) for x in range(1, 97)]

        return result

    def __get_url_all(self, url_base):
        """
        循环处理 url_base，获取所有效果图页面的地址
        :param url_base: list 效果图母页面地址集合
        :return: None
        """

        for one in url_base:
            r = request.urlopen(one)
            contents = r.read()
            contents = str(contents, encoding='utf-8')
            result = re.findall(self.pattern_top, contents)
            temp = lambda x: {'a': x.split('">')[0], 'n': x.split('">')[1]}
            result_list = map(temp, result)
            self.url_all.extend(result_list)

    def go(self):
        """
        入口方法
        """
        # 获取 url_base
        url_base = self.__get_url_base()

        # url_all (list)：循环处理 url_base，获得所有效果图页面地址，存入 url_all 中
        # self.__get_url_all(url_base)
        # 先跳过函数 get_url_all 以节省带宽：制作临时假数据，测试连接和爬虫（get_url_all 函数已完成）
        self.url_all = [{'a': '5767', 'n': '朝阳区南沙滩路3号 350.0平 四居'}, {'a': '6197', 'n': '密云云秀花园 350.0平 别墅'}]


spider = SpiderToday()
spider.go()
print("File Copy Successful!!!")
