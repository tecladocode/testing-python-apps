from section10.video_code.tests.acceptance.page_model.blog_page import BlogPageLocators
from section10.video_code.tests.acceptance.pages.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)
