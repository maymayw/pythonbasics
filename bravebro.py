from time import sleep
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.binary_location = 'C:\\Program Files (x86)\\BraveSoftware\Brave-Browser\\Application\\brave.exe'
# driver_exe = './chromedriver.exe'
# bravebro = webdriver.Chrome(options=chrome_options, executable_path=driver_exe)
# bravebro.get('https://dataroma.com/m/ins/ins.php?t=d&am=0&sym=&o=a&d=d')

from selenium.webdriver import chrome
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':

    # settings from Brave browser
    options = ChromeOptions()
    options.binary_location = 'C:\\Program Files (x86)\\BraveSoftware\Brave-Browser\\Application\\brave.exe'

    # anti selenium detection
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver_path = './chromedriver.exe'
    braveBro = webdriver.Chrome(options=options, executable_path=driver_path)

    url = 'http://www.google.com'
    braveBro.get(url)
    sleep(2)
    braveBro.quit()

    url = 'https://flightaware.com'
    options.add_argument('headless')
    braveBro = webdriver.Chrome(options=options, executable_path=driver_path)
    braveBro.get(url)
    sleep(2)
    braveBro.save_screenshot('2.png')
    braveBro.quit()


