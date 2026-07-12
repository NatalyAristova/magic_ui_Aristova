from pages.base_page import BasePage
from pages.locators import category_desk_locators as cat_loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Category(BasePage):
    page_url = 'shop/category/desks-1'


    def search_table(self, text):
        self.search(cat_loc.search_field, text)


    def check_search_alert(self, text):
        found_item = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(cat_loc.found_table)))
        assert text in found_item.text


    def click_checkbox(self, locator):
        checkbox = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)))
        self.driver.execute_script("arguments[0].click();", checkbox)


    def check_item(self, locator, text):
        found_item = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)))
        assert found_item.text == text


    def add_item_to_cart(self):
        cart = self.find(cat_loc.cart)
        table = self.find(cat_loc.table)
        actions = ActionChains(self.driver)
        actions.move_to_element(table)
        actions.click(cart)
        actions.perform()


    def check_added_item(self):
        table_name = self.find(cat_loc.table_name)
        modal = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((cat_loc.modal)))
        assert table_name.text in modal.text
