from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')


@then('There is a (.*) tag with the content "(.*)"')
def step_impl(context, tag_name, tag_content):
    tag = context.browser.find_element(By.XPATH, '//{}[text()="{}"]'.format(tag_name, tag_content))
    assert tag is not None
