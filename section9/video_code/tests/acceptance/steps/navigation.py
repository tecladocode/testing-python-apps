from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/')


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:5000/blog')


@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.browser.find_element_by_id(link_id) # find_element_by_link_text can also work
    link.click()


@then('I am on the homepage')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/'


@then('I am on the blog page')
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:5000/blog'
