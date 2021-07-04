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

file = open('MOTLEYFOOL_NEWS_DATA_RAW.txt', 'w')
writer = csv.writer(file, delimiter = ',')

path = "./chromedriver"
driver = webdriver.Chrome(path, options = options)

url = "https://www.fool.com/quote/nasdaq/advanced-micro-devices/amd/"
driver.get(url)

time.sleep(2)


print("Motley Fool Scraper Starting...")
button = True
print("--preparing--page--for--scraping--")
while(button == True):
	try:
		buttons = driver.find_element_by_css_selector("#load-more").click()#("load-more").click()
		time.sleep(.3)
	except:
		button = False
		print("NO MORE BUTTONS TO CLICK (OR) PAGE LOADED TOO SLOWLY...")
		news = driver.find_elements_by_class_name("text")
		for post in tqdm(news):
			date = post.find_element_by_class_name("story-date-author").text
			headline = post.find_element_by_css_selector("[data-id='article-list-hl']").text
			writer.writerow([headline,date])

file.close()
driver.quit()
