import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

class BasePageObject(object):
  url = 'https://internal-tools-app1-staging.east:3000/protocols/8zbH2xjAL4WuTdLfF/run'

  def __init__(self, driver):
      self.driver = driver

  def fill_form_by_css(self, locator, value):
      elem = self.driver.find_element(By.CSS_SELECTOR, locator)
      elem.clear()
      elem.send_keys(value)
      time.sleep(1)

  def find_by_css(self, locator):
      return self.driver.find_element(By.CSS_SELECTOR, locator)

  def wait_for_element_by_css(self, locator,timeout=20):
      ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

  def navigate(self):
      self.driver.get(self.url)
