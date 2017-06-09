from behave import *

@given(u'we search by an existing vial_barcode_id')
def step_impl(context):
    pass

@then('we should see that {form_id} displayed as {type}')
def step_impl(context,form_id,type):
    pass

@then('we should be able to set {type} in {form_id}')
def step_impl(context):
    pass

@then(u'we should be able to submit it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we should be able to submit it')
