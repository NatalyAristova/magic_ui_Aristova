from pages.base_page import BasePage
from pages.locators import category_desk_locators as cat_loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Category(BasePage):
    page_url = 'shop/category/desks-1'


    def search_table(self, text):
        search_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(cat_loc.search_field))
        self.driver.execute_script("arguments[0].value = arguments[1];", search_field, text)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}))",
                                   search_field)
        self.driver.execute_script("arguments[0].form.submit()", search_field)


    def check_search_alert(self, text):
        found_item = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(cat_loc.found_table)))
        assert text in found_item.text


    def click_steel_checkbox(self):
        checkbox = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(cat_loc.steel_checkbox)))
        self.driver.execute_script("arguments[0].click();", checkbox)


    def assert_steel_item(self):
        found_item = (WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(cat_loc.steel_table)))
        assert found_item.text == 'Customizable Desk'


    def add_item_to_cart(self):
        cart = self.find(cat_loc.cart)
        table = self.find(cat_loc.table)
        actions = ActionChains(self.driver)
        actions.move_to_element(table)
        actions.click(cart)
        actions.perform()
        table_name = self.find(cat_loc.table_name)
        modal = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((cat_loc.modal)))
        assert table_name.text in modal.text
