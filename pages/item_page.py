from pages.base_page import BasePage
from pages.locators import item_page_locators as item_loc
from selenium.webdriver.support.wait import WebDriverWait


class Item(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def add_item(self):
        add_button = self.find(item_loc.plus_button)
        self.driver.execute_script("arguments[0].click();", add_button)


    def remove_item(self):
        minus_button = self.find(item_loc.remove_button)
        self.driver.execute_script("arguments[0].click();", minus_button)


    def assert_item_amount(self, number):
        WebDriverWait(self.driver, 10).until(
            lambda d: int(
                d.execute_script(
                    "return arguments[0].value;",
                    self.find(item_loc.items_amount)
                )
            ) == number
        )


    def get_breadcrumbs(self):
        return self.breadcrumbs(item_loc.breadcrumbs)


    def check_breadcrumbs(self):
        breadcrumbs_text = self.get_breadcrumbs()
        assert 'All Products' in breadcrumbs_text
        assert 'Multimedia' in breadcrumbs_text
        assert 'Office Design Software' in breadcrumbs_text
