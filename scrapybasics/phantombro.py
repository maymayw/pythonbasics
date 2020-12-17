from selenium import webdriver
from time import sleep
import time
if __name__ == '__main__':
    url = 'https://flightaware.com'
    # 发起请求前，可以让url表示的页面动态加载出更多的数据
    path = r'C:\Users\may\PycharmProjects\pythonbasics\phantomjs.exe'
    # 创建无界面的浏览器对象
    bro = webdriver.PhantomJS(path)
    # 发起url请求
    bro.get(url)
    time.sleep(3)
    # 截图
    bro.save_screenshot('1.png')