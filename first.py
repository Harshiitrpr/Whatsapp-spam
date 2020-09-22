from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
print(driver.title)

search_text = 'I love you 3000'

search = driver.find_element_by_name("q")
search.send_keys(search_text)
search.send_keys(Keys.RETURN)

try:
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"rso"))
    )

    articles = items.find_elements_by_class_name("g")
    print(len(articles))
    for article in articles:
        print(article.text)
finally:
    driver.quit()