def test_check_text_for_empty_cart(cart_page):
    cart_page.open_page()
    assert cart_page.empty_card_text_is() == 'Your cart is empty!'


def test_search_field_exist(cart_page):
    cart_page.open_page()
    search_field = cart_page.search_input()
    assert search_field.is_displayed()


def test_breadcrumbs(cart_page):
    cart_page.open_page()
    breadcrumbs_text = cart_page.breadcrumbs()
    assert 'Order' in breadcrumbs_text
    assert 'Shipping' in breadcrumbs_text
    assert 'Payment' in breadcrumbs_text
