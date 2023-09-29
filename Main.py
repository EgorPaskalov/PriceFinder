from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

websites = {
    "Citilink": "https://www.citilink.ru",
    "М.Видео": "https://www.mvideo.ru",
    "Юлмарт": "https://www.ulmart.ru",
    "Озон": "https://www.ozon.ru"
    }

wish = 'Телефон' #input('Что вас интересует? Напишите конкретное название товара, и если нужно, его описание')


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

for site, url in websites.items():
    driver.get(url)
    
    if site == "Citilink":
        search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/form/div/div/label/input')))
        search.send_keys(wish)
        search.send_keys(Keys.ENTER)
        description = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/a')
        price = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/main/div[1]/div/div[2]/section/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/a')
        print(description)
        driver.quit()
    # elif site == "М.Видео":
    #     price_element = driver.find_element_by_xpath("//div[@class='c-pdp-price__current']")
    #     price = price_element.text
    # elif site == "Юлмарт":
    #     price_element = driver.find_element_by_css_selector(".b-price__num")
    #     price = price_element.text
    # elif site == "Озон":
    #     price_element = driver.find_element_by_xpath("//span[@class='c2h5']")
    #     price = price_element.text
    
    # # Выводим результаты
    # print(f"Сайт: {site}")
    # print(f"Цена: {price}")
    # print("")

