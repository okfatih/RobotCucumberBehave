

@given(u'launch browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given launch browser')


@when(u'open orange hrm homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When open orange hrm homepage')


@then(u'verify that the logo present on page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the logo present on page')


@then(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')
