from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')


    def find(self, locator: tuple):
        return self.driver.find_element(*locator)


    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)


    def breadcrumbs(self, locator):
        crumbs = (WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator)))
        return crumbs.text


    def search(self, locator, text):
        search_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].value = arguments[1];", search_field, text)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}))",
                                   search_field)
        self.driver.execute_script("arguments[0].form.submit()", search_field)
