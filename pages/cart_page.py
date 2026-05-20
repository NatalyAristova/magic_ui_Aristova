from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Cart(BasePage):
    page_url = 'shop/cart'


    def empty_card_text_is(self):
        text_window = (WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(loc.empty_cart_text_loc)))
        return text_window.text


    def search_input(self):
        loupe = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(loc.loupe_loc)
        )
        self.driver.execute_script("arguments[0].click();", loupe)
        search_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(loc.search_window_loc))
        return search_field


    def breadcrumbs(self):
        crumbs = (WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(loc.breadcrumbs_loc)))
        return crumbs.text


    def cart_page_title(self):
        title = (WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(loc.cart_title_loc)))
        return title.text
