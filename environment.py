from selenium import webdriver
from pageObjects.cliapo import CliaPO


def before_all(context):
    set_environment_variables(context)
    webdriver_init(context)
    clia_signin(context)

def navigate_to_accessioner(context):
    clia_signin(context)

def clia_signin(context):
    clia_po = CliaPO(context.browser)
    clia_po.navigate()
    clia_po.login(context.clia_login_user, context.clia_login_pass)

def webdriver_init(context):
    # Setting to ignore certs
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # ChromeDriver setup
    context.browser = webdriver.Chrome(chrome_options=options)

def set_environment_variables(context):
    context.clia_login_user = 'ezequiel.uhrig@ubiome.com'
    context.clia_login_pass = 'worktrial'
