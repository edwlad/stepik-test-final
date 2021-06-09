class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def is_element_present(self, how, what):
        return bool(self.browser.find_elements(how, what))
        # try:
        #     self.browser.find_element(how, what)
        # except (имя исключения):
        #     return False
        # return True
