from behave import *
from selenium import webdriver

use_step_matcher('re')

BASE_URL = 'http://127.0.0.1:5000/'


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)


@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('{}blog'.format(BASE_URL))


@given('I am on the new post page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('{}post'.format(BASE_URL))


@then('I am on the homepage')
def step_impl(context):
    assert context.browser.current_url == BASE_URL


@then('I am on the blog page')
def step_impl(context):
    assert context.browser.current_url == '{}blog'.format(BASE_URL)
