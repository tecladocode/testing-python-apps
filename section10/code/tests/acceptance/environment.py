from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')


def after_all(context):
    context.driver.quit()
