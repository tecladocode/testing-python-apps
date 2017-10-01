from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

use_step_matcher('re')


@given('I wait for the posts to load')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'posts'))
        )
    except:
        raise Exception()
