from time import sleep
import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import ChromeOptions
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image

if __name__ == '__main__':

    # settings from Brave browser
    options = ChromeOptions()
    options.binary_location = 'C:\\Program Files (x86)\\BraveSoftware\Brave-Browser\\Application\\brave.exe'

    # anti selenium detection
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # hide the browser
    options.add_argument('headless')

    driver_path = 'C:\\Users\\may\\PycharmProjects\\pythonbasics\\chromedriver.exe'
    braveBro = webdriver.Chrome(options=options, executable_path=driver_path)
    braveBro.set_window_size(1600,900)

    url = 'https://flightaware.com'
    braveBro.get(url)

    # scroll and set timeframe to year
    trendgraph = braveBro.find_element_by_class_name('flight-stats-inner')
    graphLocation = trendgraph.location

    # mediaAttri = braveBro.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[2]')
    # mediaAttriLocation = mediaAttri.location

    height = trendgraph.size['height']

    # trandMessage = braveBro.find_element_by_xpath('/html/body/div[1]')
    width = trendgraph.size['width']


    scrollScript = 'window.scrollTo(0, %d)'%graphLocation['y']
    braveBro.execute_script((scrollScript))

    # button = braveBro.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[1]/div[1]/div[2]/div[2]/span/div/a/span[2]/b')
    button = braveBro.find_element_by_class_name('select2-choice')
    button.click()

    actions = ActionChains(braveBro)
    for i in range(0,2):
        actions.send_keys(Keys.DOWN).perform()
    actions.send_keys(Keys.RETURN).perform()
    sleep(2)


    # save whole screenshot
    imageName = 'flightaware.png'
    braveBro.save_screenshot('C:/Users/may/PycharmProjects/pythonbasics/FlightAware/'+imageName)

    # # crop trend and save with date

    range = (0,0,width,height)
    img = Image.open('C:/Users/may/PycharmProjects/pythonbasics/FlightAware/'+imageName)
    frame = img.crop(range)
    today = datetime.today().strftime('%Y%m%d')
    frame.save('C:/Users/may/PycharmProjects/pythonbasics/FlightAware/'+today+imageName)
    img.close()

    braveBro.quit()


