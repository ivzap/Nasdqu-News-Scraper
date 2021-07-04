from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import csv

choice = input("Are you sure you want to start program, csv's may be overwritten? (y = yes , n = no): ")
if choice == "n":
	exit()

global news
options = Options()
#options.add_argument('--headless')
#options.add_argument('window-size=1920x1080');

file = open('NASDAQ_NEWS_DATA_RAW.txt', 'w')
writer = csv.writer(file, delimiter = ',')

path = "./chromedriver"
driver = webdriver.Chrome(path, options = options)

url = "https://www.nasdaq.com/market-activity/stocks/bb/news-headlines"
driver.get(url)

time.sleep(2)

cookies = driver.find_element_by_id("_evidon-decline-button").click()
pages = int(driver.find_element_by_css_selector("body > div.dialog-off-canvas-main-canvas > div > main > div.page__content > div.quote-subdetail__content.quote-subdetail__content--new > div:nth-child(3) > div > div.quote-subdetail__indented-components > div > div.quote-news-headlines.quote-news-headlines--paginated > div > div > div > button:nth-child(9)").text)
print("NASDAQ SCRAPER STARTING...")
for page in tqdm(range(1,pages+1)):
	try:
		news = driver.find_elements_by_class_name("quote-news-headlines__item")
		for post in news:
			header = post.find_element_by_class_name("quote-news-headlines__item-title").text
			date = post.find_element_by_class_name("quote-news-headlines__date").text
			if header and post != " ":
				writer.writerow([header,date])
		button = driver.find_element_by_xpath("/html/body/div[2]/div/main/div[2]/div[4]/div[3]/div/div[1]/div/div[1]/div/div/button[2]").click()
		time.sleep(1.5)
		#writer.writerow({'header':header, 'date':date})

	except:
		print("Couldn't find element")

print("NASDAQ SCRAPER FINISHED.")
file.close()
driver.quit()
