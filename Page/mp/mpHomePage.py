from Base.base import Base
from Page.mp.pageElements import PageElements


class MpHomePage(Base):
    def __init__(self):
        Base.__init__(self, 'mp')

    def get_company_name(self):
        # 获取公司的名字
        company_name = self.search_ele(PageElements.home_company_name_class).text
        return company_name

    def content_manage(self):
        # 点击进入管理页面
        self.click_ele(PageElements.home_content_manage_xpath)

    def publish_article(self):
        # 点击发布文章
        self.click_ele(PageElements.home_publish_article_xpath)
