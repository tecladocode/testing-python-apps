from section10.video_code.tests.acceptance.page_model.base_page import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1'

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    @property
    def title(self):
        return self.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.find_elements(*BasePageLocators.NAV_LINKS)
