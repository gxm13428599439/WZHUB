"""
by gxm
2021/11/23
"""

import time   #导入time
from selenium.webdriver.common.by import By  #部分导入selenium里的webdriver里的By命令
def exec_search(driver,url,name,passwd,key):
    driver.get(url)   #打开ERP的网址
    driver.maximize_window()     #最大化窗口
    driver.find_element(By.NAME,"username").send_keys(name)   #通过username属性定位元素，输入用户名
    driver.find_element(By.ID,"password").send_keys(passwd)    #定位ID属性定位元素，输入密码
    driver.find_element(By.ID,"btnSubmit").click()
    log_name= driver.find_element(By.XPATH,"//p").text
    driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
    id=driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute("id")    #获取零售出库父级（/..）的id
    iframe_id=id+'-frame'     #拼接得到iframe_id
    driver.switch_to.frame(iframe_id)   #通过ID进行iframe子页面的切换
    driver.find_element(By.NAME,"searchNumber").send_keys(key)    #iframe页面嵌套先切换到子页面才可以,输入566
    driver.find_element(By.XPATH,'//span[text()="查询"]').click()    #点击“查询”按钮
    time.sleep(2)
    text1=driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return text1