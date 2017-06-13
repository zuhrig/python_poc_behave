from basepo import BasePageObject
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from IPython import embed

class AccessionerPO(BasePageObject):
    main_css_selector = 'div.x_panel'
    select_list_css = "[name='supervisor']"
    sample_id_input_css = '#s2id_autogen2'
    tubename = "testtube"
    tubeundefined_css = '#sample-tubeundefined'

    def set_random_supervisor(self):
        self.wait_for_element_by_css(self.select_list_css)
        select_list = Select(self.find_by_css(self.select_list_css))
        # we dont wont to get the placeholder
        select_list.select_by_index(randint(1, 9))

    def set_sample_id(self):
        self.wait_for_element_by_css(self.sample_id_input_css)
        self.fill_form_by_css(self.sample_id_input_css, "testtube")
        self.find_by_css(self.sample_id_input_css).send_keys(u'\ue00d')

    def is_tubeundefined_displayed(self):
        self.wait_for_element_by_css(self.tubeundefined_css)
        return self.find_by_css(self.tubeundefined_css).is_displayed()
