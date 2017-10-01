from selenium.webdriver.common.by import By


class BlogPageLocators:
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'
