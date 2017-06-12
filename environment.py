from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def before_all(context):
    # Setting to ignore certs
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # ChromeDriver setup
    context.browser = webdriver.Chrome(chrome_options=options)
    # CLIA login
    login_clia(context)
    go_to_clia_protocols_list(context)
    go_to_clia_accessioner_protocol(context)

#TODO: belongs to a CliaPageObject.login
def login_clia(context):
    # var setup
    context.clia_url = 'https://internal-tools-app1-staging.east:3000'
    clia_login_user = 'ezequiel.uhrig@ubiome.com'
    clia_login_pass = 'worktrial'
    field_set_css_selector = '#login > section > form > fieldset'
    dashboard_main_css_selector = 'body > section > div'
    user_input_css_selector = '#login > section > form > fieldset > div:nth-child(2) > input'
    pass_input_css_selector = '#login > section > form > fieldset > div:nth-child(3) > input'
    submit_button_css_selector = '#login > section > form > fieldset > div:nth-child(4) > button'
    
    # driver actions
    context.browser.get(context.clia_url)
    ui.WebDriverWait(context.browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, field_set_css_selector)))
    
    # element find/setup
    user_input = context.browser.find_element(By.CSS_SELECTOR, user_input_css_selector)
    pass_input = context.browser.find_element(By.CSS_SELECTOR, pass_input_css_selector)
    submit_button = context.browser.find_element(By.CSS_SELECTOR, submit_button_css_selector)
    
    # elements actions
    user_input.send_keys(clia_login_user)
    pass_input.send_keys(clia_login_pass)
    submit_button.click()
    ui.WebDriverWait(context.browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dashboard_main_css_selector)))

#TODO: belongs to a CliaPageObject.go_to_protocol_list
def go_to_clia_protocols_list(context):
    protocol_list_css_selector = 'body > section > div > div.right_col > div > div.row > div > div > div > table'
    context.browser.get(context.clia_url + '/protocols')
    ui.WebDriverWait(context.browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, protocol_list_css_selector)))

#TODO: belongs to a CliaPageObject.go_to_clia_accessioner_protocol
def go_to_clia_accessioner_protocol(context):
    context.browser.get(context.clia_url + '/protocols/8zbH2xjAL4WuTdLfF/run')
    accessioner_main_css_selector = '#s2id_autogen2'
    ui.WebDriverWait(context.browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, accessioner_main_css_selector)))
