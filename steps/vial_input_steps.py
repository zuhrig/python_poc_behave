from behave import *

@when('we search by an existing {id}')
def step_impl(context,id):
    pass

@then('we should see that {id} info displayed')
def step_impl(context,id):
    pass

@given(u'I set a random supervisor')
def step_impl(context):
    context.accessioner_po.set_random_supervisor()

@given(u'I set a testtube')
def step_impl(context):
    context.accessioner_po.set_sample_id()

@then(u'I should see the sample-tubeundefined table')
def step_impl(context):
    assert context.accessioner_po.is_tubeundefined_displayed(), "[ERROR] table not found"
