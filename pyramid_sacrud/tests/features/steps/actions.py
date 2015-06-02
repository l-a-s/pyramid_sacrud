from behave import then, when, given


@given(u'Create user form')
def step_impl(context):
    context.driver.get(context.URL + 'user/create/')


@given(u'Update user form {name}')
def step_impl(context, name):
    user = context.dbsession.query(
        context.models['user']).filter_by(name=name).one()
    context.driver.get(context.URL + 'user/update/id/{}'.format(user.id))


@when(u'Change user name to {name}')
def step_impl(context, name):
    name_field = context.driver.find_element_by_xpath(
        ".//*[starts-with(@id, 'deformField') and @name='name']"
    )
    name_field.clear()
    name_field.send_keys(name)
    context.driver.find_element_by_xpath(
        "//*[@name = 'form.submitted']"
    ).click()
    context.user = context.dbsession.query(
        context.models['user']).filter_by(name=name).one()


@when(u'Delete user {name}')
def step_impl(context, name):
    user = context.dbsession.query(
        context.models['user']).filter_by(name=name).one()
    context.user_id = user.id
    context.driver.get(context.URL + 'user/delete/id/{}'.format(user.id))


@then(u'I should find user in user table')
def step_impl(context):
    user = context.user
    context.driver.get(context.URL + 'user/update/id/{}'.format(user.id))
    assert user.name in context.driver.page_source


@then(u"I don't want find user in user table")
def step_impl(context):
    user_id = context.user_id
    user = context.dbsession.query(
        context.models['user']).filter_by(id=user_id).first()
    assert user is None
    context.driver.get(context.URL + 'user/update/id/{}'.format(user_id))
    assert '404' in context.driver.page_source
