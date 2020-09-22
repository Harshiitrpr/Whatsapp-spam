from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = "Neha"

string = "Hi, Neha"

time.sleep(6)

x_arg = '//span[@title="' + target + '"]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

online = '//span[@title="online"]'

while(True):
    isonline = driver.find_elements_by_xpath(online)
    if(len(isonline)):
        input_box.send_keys('Sorry for bothering, '+ target + ' It was an automated program which sends this message until you are shown online.' + Keys.ENTER)
        break
    else:
        input_box.send_keys(string + Keys.ENTER)
        time.sleep(0.5)
