import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = "Alex"
        last_name = "Filatov"
        email = "alexfilatov@gmail.com"
        mobile = "1234567890"
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys("English")
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r"C:\Users\alexa\PycharmProjects\Test_Project_2\sending_file")
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("Russia, Moscow")
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(10)

