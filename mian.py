
import sys
import os
from scrapy.cmdline import execute

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    #print(os.path.dirname(os.path.abspath(__file__)))  #os.path.dirname获取当前文件的父目录, os.path.abspath获取当前文件的路径
    execute(["scrapy","crawl","lianjia"])
