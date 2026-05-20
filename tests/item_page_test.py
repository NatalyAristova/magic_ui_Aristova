def test_breadcrumbs(item_page):
    item_page.open_page()
    breadcrumbs_text = item_page.breadcrumbs()
    assert 'All Products' in breadcrumbs_text
    assert 'Multimedia' in breadcrumbs_text
    assert 'Office Design Software' in breadcrumbs_text


def test_add_item(item_page):
    item_page.open_page()
    item_page.add_item()
    item_page.assert_item_amount(2)


def test_remove_item(item_page):
    item_page.open_page()
    item_page.remove_item()
    item_page.assert_item_amount(1)
