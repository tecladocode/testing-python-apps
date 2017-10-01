from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert tag is not None
    assert tag.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert tag.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    tag = context.browser.find_element_by_id('posts')

    assert tag.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    tags = context.browser.find_elements(By.CLASS_NAME, 'post-link')

    posts_with_title = [post for post in tags if post.text == title]

    assert len(posts_with_title) > 0
