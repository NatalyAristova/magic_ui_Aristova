from pages.cart_page import Cart
from pages.category_page import Category
from pages.item_page import Item
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def cart_page(driver):
    return Cart(driver)


@pytest.fixture()
def category_page(driver):
    return Category(driver)


@pytest.fixture()
def item_page(driver):
    return Item(driver)
