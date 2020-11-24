import pytest

from Base.base import Base
from Page.mp.pageElements import PageElements
import time


class MpPublishArticle(Base):
    def __init__(self):
        Base.__init__(self, 'mp')

    def publish_article(self, title, content, channel_text):
        # 输入标题
        self.send_ele(PageElements.publish_article_title_css, title)
        # 切换到frame
        self.driver.switch_to.frame(PageElements.publish_article_frame)
        # 输入内容
        self.send_ele(PageElements.publish_article_content_id, content)
        # 切换回原页面
        self.driver.switch_to.default_content()
        # 点击封面 选择无图
        self.click_ele(PageElements.publish_article_fm_xpath)
        # 点击选择频道
        self.select_channel(PageElements.publish_article_select_css,
                            PageElements.publish_article_channel_list_xpath, channel_text)
        # self.click_ele(PageElements.publish_article_channel_xpath)
        # 点击发布
        time.sleep(2)
        self.click_ele(PageElements.publish_article_btn_xpath)
