from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

class Site:
    def __init__(self, url, search_xpath, item_card_xpath, price_xpath):
        self.url = url
        self.search_xpath = search_xpath
        self.item_card_xpath = item_card_xpath
        self.price_xpath = price_xpath
        
websites = {
    "Citilink": Site('https://www.citilink.ru',
    '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input',
    '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/a',
    '//*[@id="__next"]/div/main/div[1]/div[2]/div/div[4]/div/div[3]/div/div[2]/div/div[1]/span/span/span[1]'),

    "М.Видео": Site("https://www.mvideo.ru",
    '//*[@id="1"]', 
    '/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-srp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/mvid-product-cards-row/div[1]/div[2]/mvid-plp-product-title/div/a',
    '/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-pdp/mvid-pdp-general/div/mvid-general-details/section/div[2]/div/div[2]/mvideoru-product-details-card[1]/div/mvid-price/div/span[1]'),
    
    # "Wildberries": Site('https://www.wildberries.ru/',
    # '//*[@id="searchInput"]',
    # '//*[@id="c178630990"]/div/a',
    # '//*[@id="3aaaff51-d9da-e833-4ac9-014928c67d63"]/div[3]/div[2]/div[1]/div/div/div/p[1]/span/ins')
    }

wish = 'Redmi 11' #input('Что вас интересует? Напишите название товара и его конкретную характеристику: ')

info = {}

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-infobars")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

wait = WebDriverWait(driver, 10)

def find_first_item_price(url:str, search_path:str , item_card_path:str, price_path:str):
    # try:
        driver.get(url)
        time.sleep(1)
        search = wait.until(EC.presence_of_element_located((By.XPATH, search_path)))
        search.send_keys(wish)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        item_card = driver.find_element(By.XPATH, item_card_path)
        item_link = item_card.get_attribute('href')
        driver.get(item_link)
        time.sleep(2)
        price = driver.find_element(By.XPATH, price_path).text
        return price, driver.current_url
    # except NoSuchElementException:
    #     print("На сайте", url, "товар не найден")
    #     return "Не найдено"

def find_best_price():
    sorted_price = sorted(info.items(), key=lambda x: x[1])
    return sorted_price

for name, site in websites.items():
    price = find_first_item_price(site.url, site.search_xpath, site.item_card_xpath, site.price_xpath)
    info[name] = price
    driver.quit
print(info)
print(find_best_price())