from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cart(BasePage):
    page_url = 'shop/cart'


    def check_empty_cart_text(self):
        text_window = (WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(loc.empty_cart_text_loc)))
        assert text_window.text == 'Your cart is empty!'


    def open_search_field(self):
        loupe = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(loc.loupe_loc)
        )
        self.driver.execute_script("arguments[0].click();", loupe)


    def get_search_input(self):
        search_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(loc.search_window_loc))
        return search_field


    def check_search_input_is_visible(self):
        self.open_search_field()
        search_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(loc.search_window_loc))
        assert search_field.is_displayed()


    def get_breadcrumbs(self):
        return self.breadcrumbs(loc.breadcrumbs_loc)


    def check_breadcrumbs(self):
        breadcrumbs_text = self.get_breadcrumbs()
        assert 'Order' in breadcrumbs_text
        assert 'Shipping' in breadcrumbs_text
        assert 'Payment' in breadcrumbs_text


    def cart_page_title(self):
        title = (WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(loc.cart_title_loc)))
        return title.text

