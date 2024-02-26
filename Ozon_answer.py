import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import undetected_chromedriver as uc
import pickle

def check_exists_by_tagname(element):
    try:
        #element.find_element(By.XPATH,'./div')
        element.find_element(By.TAG_NAME, 'div')
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(driver, show_more):
    try:
        driver.find_element(By.XPATH, show_more)
        #element.find_element(By.TAG_NAME, 'div')
    except NoSuchElementException:
        return False
    return True

url = "https://seller.ozon.ru/app/dashboard/main"
options = uc.ChromeOptions()
#options.set_preference("general.useragent.override", f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0")
#options.set_preference('dom.webdriver.enabled',False)
#options.add_argument("--disable-blink-features")
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#driver = webdriver.Chrome(options=options)
driver = uc.Chrome(options=options)
#driver = webdriver.Firefox('C:\\Users\\Makar\\PycharmProjects\\Ozon2\\.venv\\geckodriver.exe')

try:
    time.sleep(1)
    driver.get(url = url)
    time.sleep(2)
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, 'button.signin_ozonIdButton_3Ya6M').click()
    # time.sleep(5)
    # #driver.find_element(By.NAME)
    # driver.find_element(By.NAME, "autocomplete").send_keys("9099159260")
    # time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR, 'button.b237-a4').click()
    # time.sleep(100)
    # pickle.dump(driver.get_cookies(), open(f"89099159260_cookies", "wb"))
    for cookie in pickle.load(open(f"89099159260_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(2)
    driver.get("https://seller.ozon.ru/app/reviews")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'div.index_tabCounter_3Tppu').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.index_controlBtn_148Gj').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'button.filter-chip-module_size-500_dRAlj').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'div.dropdown-item-module_size-500_pB5xD').click()
    time.sleep(2)
    #elements = driver.find_elements(By.CSS_SELECTOR, 'div.index_review_MIfmk')
    count = 0
    show_more = '/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/button'
    while check_exists_by_xpath(driver, show_more) == True:
        #elements = driver.find_elements(By.CSS_SELECTOR, 'div.index_review_MIfmk')
        #count = 1
        #for element in elements:
        count += 1
        element = driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{count}]/td[6]/div/button')
        if check_exists_by_tagname(element) == False:
            #time.sleep(10)
            #element.find_elements(By.CSS_SELECTOR, 'button.link-module_linkPseudo_v65P8').click()
            driver.find_element(By.XPATH, f'//*[@id="app"]/main/div[1]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{count}]/td[6]').click()
            time.sleep(3)
            if check_exists_by_xpath(driver, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[15]/textarea') == True:
                driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[15]/textarea').send_keys("Здравствуйте! Спасибо за отзыв. Рады, что Вы остались довольны товаром. Спасибо за Вашу поддержку и лояльное отношение к товарам бренда. Всего наилучшего и удачных покупок! С уважением, команда IN HOME.")
                time.sleep(2)
                driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[15]/div[3]/button').click()
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, 'div.index_close_2j0Nf').click()
                time.sleep(1)
            elif check_exists_by_xpath(driver, '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[16]/textarea') == True:
                driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[16]/textarea').send_keys("Здравствуйте! Спасибо за отзыв. Рады, что Вы остались довольны товаром. Спасибо за Вашу поддержку и лояльное отношение к товарам бренда. Всего наилучшего и удачных покупок! С уважением, команда IN HOME.")
                time.sleep(2)
                driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[16]/div[3]/button').click()
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, 'div.index_close_2j0Nf').click()
                time.sleep(1)

        #time.sleep(3)
        if count % 10 == 0 and count % 1500 != 0:
            time.sleep(1)
            driver.find_element(By.XPATH, show_more).click()
            time.sleep(3)
        if count % 1500 == 0:
            count = 0
            driver.refresh()
            time.sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[1]/div/div/div[2]/div[2]/button[2]').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, 'button.filter-chip-module_size-500_dRAlj').click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, 'div.dropdown-item-module_size-500_pB5xD').click()
            time.sleep(2)



    # for tag in element:
    #     if check_exists_by_css(driver, 'div.table_wrapper_BIPDB'):
    #         count = 1
    #         print(1)
    # if count == 0:
    #     time.sleep(5)
    #     element.click()
    #     time.sleep(5)
    #     driver.find_element(By.CSS_SELECTOR, 'div.index_close_2j0Nf').click()

    #driver.find_element(By.xpath("//button[@button type=submit]")).click()
    time.sleep(1000)
except Exception as ex:
    print(ex)
finally:
    driver.close();
    driver.quit();