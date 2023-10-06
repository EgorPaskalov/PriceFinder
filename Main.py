from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

city_link_search_xpath = '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input'

class Site:
    def __init__(self, url, search_xpath, price_xpath):
        self.url = url
        self.search_xpath = search_xpath
        self.price_xpath = price_xpath
        
websites = {
    "Citilink": Site('https://www.citilink.ru',
    '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input',
    '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div/div[3]/div[3]/button/span/div[2]/span/span/span[1]'),
    "М.Видео": "https://www.mvideo.ru",
    "Юлмарт": "https://www.ulmart.ru",
    "Озон": "https://www.ozon.ru"
    }

wish = 'Iphone 15 Pro 128GB' #input('Что вас интересует? Напишите конкретное название товара, и если нужно, его описание')

info = {}

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

def find_first_item_price(url:str, search_path:str , price_path:str):
    driver.get(url)
    search = wait.until(EC.presence_of_element_located((By.XPATH, search_path)))
    search.send_keys(wish)
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    price = driver.find_element(By.XPATH, price_path).text
    return price

for name, site in websites.items():
    find_first_item_price(site.url, site.search_xpath, site.price_xpath)
    
    # elif site == "Юлмарт":
        # search = wait.until(EC.presence_of_element_located((By.XPATH, '')))
        # search.send_keys(wish)
        # search.send_keys(Keys.ENTER)
    
    # elif site == "Озон":
    #     price_element = driver.find_element_by_xpath("//span[@class='c2h5']")
    #     price = price_element.text
    driver.quit
print(info, "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")


