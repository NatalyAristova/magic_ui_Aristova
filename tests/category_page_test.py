def test_table_searching(category_page):
    category_page.open_page()
    category_page.search_table('Cust')
    category_page.check_search_alert('Cust')


def test_steel_table_searching(category_page):
    category_page.open_page()
    category_page.click_steel_checkbox()
    category_page.assert_steel_item()


def test_selected_table_in_modal(category_page):
    category_page.open_page()
    category_page.add_item_to_cart()

