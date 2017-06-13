from basepo import BasePageObject
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

class CliaPO(BasePageObject):
    field_set_css_selector = '#login > section > form > fieldset'
    main_css_selector = 'body > section > div'
    user_css_selector = '#login > section > form > fieldset > div:nth-child(2) > input'
    pass_css_selector = '#login > section > form > fieldset > div:nth-child(3) > input'
    submit_css_selector = 'button.btn.btn-default.submit.login'


    def navigate(self):
        self.driver.get(self.url)
        self.wait_for_element_by_css(self.field_set_css_selector)

    def login(self, user, password):
        self.wait_for_element_by_css(self.field_set_css_selector)
        self.fill_form_by_css(self.user_css_selector, user)
        self.fill_form_by_css(self.pass_css_selector, password)

        self.driver.execute_script("$('button.btn.btn-default.submit.login').submit()")

        try:
            time.sleep(3)
            self.driver.switch_to_alert().accept()
            self.driver.execute_script("$('button.btn.btn-default.submit.login').submit()")
        except NoAlertPresentException as e:
            print("no alert")


    def navigate_to_protocols(self):
        self.driver.get(self.url + '/protocols')
