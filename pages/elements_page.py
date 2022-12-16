import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Dmytro')
        self.element_is_visible(self.locators.EMAIL).send_keys('d.zadnepryansky@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Chernivtsi')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Kharkiv')
        self.element_is_visible(self.locators.SUBMIT).click()
