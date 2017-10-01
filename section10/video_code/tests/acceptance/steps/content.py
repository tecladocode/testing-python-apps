from behave import *

from section10.video_code.tests.acceptance.pages.base_page import BasePage
from section10.video_code.tests.acceptance.pages.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    tag = page.title
    assert tag is not None
    assert tag.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    tag = page.title
    assert tag.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.browser)
    tag = page.posts_section

    assert tag.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.browser)
    tags = page.posts

    posts_with_title = [post for post in tags if post.text == title]

    assert len(posts_with_title) > 0
    # assert posts_with_title[0].is_displayed()
