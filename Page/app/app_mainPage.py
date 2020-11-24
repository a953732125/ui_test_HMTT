from Base.base import Base
from Page.app.pageElements import PageElements


class AppMainPage(Base):
    def __init__(self):
        Base.__init__(self, 'app')

    def select_banner_channel(self, text):
        self.app_swipe_area(PageElements.main_banner_area_class,
                            PageElements.main_banner_select_channel_xpath, text, tag=3)
