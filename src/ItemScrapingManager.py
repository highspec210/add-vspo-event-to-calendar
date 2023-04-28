from datetime import datetime
from ItemModel import ItemModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import re


class ItemScrapingManager:
    @staticmethod
    def scrap_item(name: str, url: str):
        date_class_name = "Product_SalesPeriod_Wrapper"

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome("chromedriver", chrome_options=options)
        driver.get(url)
        sleep(10)
        for element in driver.find_elements(By.CLASS_NAME, date_class_name):
            for element_p in element.find_elements(By.CSS_SELECTOR, "p"):
                date_time_list = re.findall(
                    "(\d{1,4})年(\d{1,2})月(\d{1,2})日 (\d{1,2})時(\d{1,2})分",
                    element_p.text,
                )
                datetime_start = ItemScrapingManager.get_datetime(
                    date_time_list[0]
                )
                datetime_end = ItemScrapingManager.get_datetime(
                    date_time_list[1]
                )
                item = ItemModel(name, url, datetime_start, datetime_end)
                return item

    @staticmethod
    def get_datetime(date_time) -> datetime:
        ret = datetime(
            int(date_time[0]),
            int(date_time[1]),
            int(date_time[2]),
            int(date_time[3]),
            int(date_time[4]),
        )
        return ret
