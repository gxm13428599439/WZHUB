"""
by gxm
2021/11/23
"""
from selenium import webdriver  #部分导入selenium里的webdriver
driver=webdriver.Chrome()     # 选择谷歌浏览器 建立一个会话  --赋值给一个变量
driver.implicitly_wait(10)      #隐式等待

from common import method  #导入公共方法
from testdata import data  #导入测试数据
url=data.testdata.get("url")
name=data.testdata.get("name")
passwd=data.testdata.get("passwd")
key=data.testdata.get("key")

result2=method.exec_search(driver=driver,url=url,name=name,passwd=passwd,key=key)
if key in result2:
    print("搜索结果正确!")
else:
    print("搜索错误！")