from section10.video_code.tests.acceptance.pages.base_page import BasePage


class PostPage(BasePage):

    def __init__(self, driver, post_title):
        super(PostPage, self).__init__(driver)
        self.post_title = post_title

    @property
    def url(self):
        return super(PostPage, self).url + '/post/' + self.post_title
