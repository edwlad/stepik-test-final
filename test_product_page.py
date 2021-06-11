import pytest
from pages.product_page import ProductPage

links = [
    # 'http://selenium1py.pythonanywhere.com/',
    # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer',
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link, 1)
    page.open()
