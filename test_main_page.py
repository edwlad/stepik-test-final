# pytest -s -v --tb=line --language=en test_main_page.py

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

links = [
    'http://selenium1py.pythonanywhere.com/',
    # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer',
    # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
]


@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page(browser, link):
    page = MainPage(browser, link, 1)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
