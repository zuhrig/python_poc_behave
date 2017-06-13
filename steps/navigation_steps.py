from behave import *
from pageObjects.accessionerpo import AccessionerPO

@given(u'we are on protocol 5330')
def step_impl(context):
    context.accessioner_po = AccessionerPO(context.browser)
