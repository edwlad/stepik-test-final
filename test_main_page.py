# pytest -s -v --tb=line --language=en test_main_page.py

import pytest
from pages.main_page import MainPage

links = [
    'http://selenium1py.pythonanywhere.com/',
]


@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page(browser, link):
    page = MainPage(browser, link)  # инициализируем Page Object
    page.open()  # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы
