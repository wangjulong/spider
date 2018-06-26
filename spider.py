import os
import shutil
import sys
from urllib import request
import re


class Spider():
    urls = []
    root_pattern = '<li><i class="arr2"></i><img src="../../([\s\S]*?)" tppabs'
    pattern_title = '<h2 class="title">([\s\S]*?)</h2>'
    dir_prefix = r'D:/BaiduNetdiskDownload/runyuanzs/runyuanzs/www.runyuanzs.com/'
    dir_image = r'D:/BaiduNetdiskDownload/runyuanzs/runyuanzs/www.runyuanzs.com/images/'

    def __get_urls(self):
        url = 'file:///D:/BaiduNetdiskDownload/runyuanzs/runyuanzs/www.runyuanzs.com/jzxl/xgt/'
        root_dir = r'D:\BaiduNetdiskDownload\runyuanzs\runyuanzs\www.runyuanzs.com\jzxl\xgt'
        dirs = os.listdir(root_dir)
        result = [url + x for x in dirs if not x.startswith('l')]
        result.pop()
        return result

    def __fetch_content(self, url):
        r = request.urlopen(url)
        contents = r.read()
        contents = str(contents)
        return contents

    def __analysis(self, contents):
        result = re.findall(self.root_pattern, contents)
        return result

    def go(self):
        self.urls = self.__get_urls()
        for url in self.urls:
            contents = self.__fetch_content(url)
            data = self.__analysis(contents)

            # 新建目录
            url_suffix = url[-9:-5]
            dir_new = os.path.join(self.dir_image, url_suffix)
            os.makedirs(dir_new, exist_ok=True)

            for image_suffix in data:
                image_dir = self.dir_prefix + image_suffix
                image_name = os.path.basename(image_dir)

                image_new = os.path.join(dir_new, image_name)
                print(image_name)
                print(image_dir)
                print(image_new)
                if os.path.exists(image_dir):
                    shutil.copyfile(image_dir, image_new)


spider = Spider()
spider.go()
