import time

from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.get_element(self.locators.FULL_NAME_FIELD_SELECTOR, select_method="visibility_located").send_keys(full_name)
        self.get_element(self.locators.EMAIL_FIELD_SELECTOR, select_method="visibility_located").send_keys(email)
        self.get_element(self.locators.CURRENT_ADDRESS_FIELD_SELECTOR, select_method="visibility_located").send_keys(current_address)
        self.get_element(self.locators.PERMANENT_ADDRESS_FIELD_SELECTOR, select_method="visibility_located").send_keys(permanent_address)
        self.get_element(self.locators.SUBMIT_BUTTON_SELECTOR, select_method="visibility_located").click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.get_element(self.locators.CREATED_FULL_NAME_SELECTOR, select_method="presence_element").text.split(':')[1]
        email = self.get_element(self.locators.CREATED_EMAIL_SELECTOR, select_method="presence_element").text.split(':')[1]
        current_address = self.get_element(self.locators.CREATED_CURRENT_ADDRESS_SELECTOR, select_method="presence_element").text.split(':')[1]
        permanent_address = self.get_element(self.locators.CREATED_PERMANENT_ADDRESS_SELECTOR, select_method="presence_element").text.split(':')[1]
        return full_name, email, current_address, permanent_address


