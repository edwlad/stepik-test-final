# pytest -s -v --tb=line --language=en test_main_page.py

import pytest

links = [
    'http://selenium1py.pythonanywhere.com/',
]


@pytest.mark.parametrize('link', links)
def test_guest_can_go_to_login_page(browser, link):
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()