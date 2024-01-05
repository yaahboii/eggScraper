from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import requests 
import time
from selenium.webdriver.common.by import By


def eggScraper():
    try:
        options = Options()
       # options.add_argument('--headless')
        chromeDriverPath = '/usr/bin/chromedriver'
        options.add_experimental_option("detach", True)
        chromeService = ChromeService()
        driver = webdriver.Chrome(service=chromeService, options=options)
        url = ('https://www.target.com/s?searchTerm=eggs+12+ct&tref=typeahead%7Cterm%7Ceggs+12+ct%7C%7C%7C')
        driver.get(url)

        print('Website connecting, scraper waking up...')
        time.sleep(5)

        print("Parsing to begin.")
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-test="product-title"]'))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        selectors = soup.select('a[data-test="product-title"]')

        

        c = 0
        non_egg_keywords = ['timer', 'color', 'dye', 'easter', 'hershey', 'candy']
        for productTitles in selectors:
            productName = productTitles.get_text().strip().lower()
            if 'egg' in productName and not any(keyword in productName for keyword in non_egg_keywords):
                c = c + 1
                print(f'Listed egg result {c}: {productName}')
            else:
                print(f'Skipped non-egg result: {productName}')

        print(f"The number of products is : {c  }")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {type(e).__name__}: {e}")

    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {e}")


    finally:
        print("Closing Connection")
        driver.quit()
       

eggScraper()
