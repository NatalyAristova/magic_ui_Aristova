from selenium.webdriver.common.by import By


empty_cart_text_loc = (By.XPATH, '//*[@class="js_cart_lines alert alert-info"]')
cart_title_loc = (By.XPATH, '//*[@class="mb-4"]')
loupe_loc = (By.XPATH, '//div[@id="o_main_nav"]//a[@title="Search"]')
search_window_loc = (By.XPATH,
                     '//*[@class="search-query form-control oe_search_box border-0 bg-light border border-end-0 p-3"]')
breadcrumbs_loc = (By.XPATH, '//*[@class="'
               'd-flex flex-column flex-md-row align-items-end align-items-md-start justify-content-center"]')
