from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id)  # find_element_by_link_text can also work
    link.click()


@step('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    field = context.browser.find_element(By.NAME, field_name)
    field.send_keys(content)


@step('I press the submit button')
def step_impl(context):
    button = context.browser.find_element_by_id('create-post')

    button.click()
