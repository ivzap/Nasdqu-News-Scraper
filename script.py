from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
#options.add_argument('--headless')
#options.add_argument('window-size=1920x1080');

path = "./chromedriver"
driver = webdriver.Chrome(path, options = options)

url = "https://www.nasdaq.com/market-activity/stocks/goog/news-headlines"
global news
driver.get(url)
time.sleep(2)
cookies = driver.find_element_by_id("_evidon-decline-button").click()
pages = int(driver.find_element_by_css_selector("body > div.dialog-off-canvas-main-canvas > div > main > div.page__content > div.quote-subdetail__content.quote-subdetail__content--new > div:nth-child(3) > div > div.quote-subdetail__indented-components > div > div.quote-news-headlines.quote-news-headlines--paginated > div > div > div > button:nth-child(9)").text)
print(pages)

for page in range(1,pages+1):
	try:
		news = driver.find_elements_by_class_name("quote-news-headlines__item")
		for post in news:
			header = post.find_element_by_class_name("quote-news-headlines__item-title").text
			date = post.find_element_by_class_name("quote-news-headlines__date").text
			print("HEADER:", header, 'DATE: ', date)

		button = driver.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/div[4]/div[3]/div/div[1]/div/div[1]/div/div/button[2]").click()
		time.sleep(0.5)	
	except:
		print("Couldn't find element")
driver.quit()
