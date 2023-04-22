from ItemListModel import ItemListModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class ItemListScrapingManager:
    @staticmethod
    def get_item_list() -> ItemListModel:
        item_list = ItemListModel()
        url = "https://store.vspo.jp/collections/all"
        item_class_name = "product-item-meta__title"
        pagination_class_name = "pagination_arrow-item"

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome("chromedriver", chrome_options=options)
        driver.get(url)
        sleep(3)
        for element in driver.find_elements(By.CLASS_NAME, item_class_name):
            item_list.add_item(
                element.text.replace("\u3000", " "),
                element.get_attribute("href"),
            )
        for element in driver.find_elements(
            By.CLASS_NAME, pagination_class_name
        ):
            if "next" in element.get_attribute("class"):
                item_list.set_next_page(
                    element.get_attribute("href"),
                )
            else:
                item_list.set_prev_page(
                    element.get_attribute("href"),
                )
        return item_list
