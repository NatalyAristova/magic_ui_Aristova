import pytest

@pytest.mark.smoke
def test_breadcrumbs(item_page):
    item_page.open_page()
    item_page.check_breadcrumbs()


@pytest.mark.regression
def test_add_item(item_page):
    item_page.open_page()
    item_page.add_item()
    item_page.assert_item_amount(2)


@pytest.mark.extended
def test_remove_item(item_page):
    item_page.open_page()
    item_page.remove_item()
    item_page.assert_item_amount(1)
