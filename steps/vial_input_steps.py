from behave import *

@given(u'we are on protocol 5330')
def step_impl(context):
    pass

@when('we search by an existing {id}')
def step_impl(context,id):
    pass

@then('we should see that {id} info displayed')
def step_impl(context,id):
    raise NotImplementedError('we should see that {id} info displayed')
