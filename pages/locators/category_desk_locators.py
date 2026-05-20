from selenium.webdriver.common.by import By


search_field = (By.XPATH, '//div[@id="products_grid"]//input[@name="search"]')
sumit_button = (By.XPATH, '(//*[@type="submit" and @class="btn oe_search_button btn btn-light"])[1]')
found_table = (By.XPATH, '//a[@class="text-primary text-decoration-none"]')
steel_checkbox = (By.XPATH, '(//aside//label[contains(normalize-space(),"Steel")])[1]')
steel_table = (By.XPATH, '//*[@class="text-primary text-decoration-none"]')
table = (By.XPATH, '//*[@alt="Customizable Desk"]')
table_name = (By.XPATH, '//*[@class="text-primary text-decoration-none"]')
cart = (By.XPATH, '//*[@class="btn btn-primary a-submit"]')
modal = (By.XPATH, '//*[@class="modal-body oe_advanced_configurator_modal"]')