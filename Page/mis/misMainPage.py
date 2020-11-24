from Base.base import Base
from Page.mis.pageElements import PageElements


class MisMainPage(Base):
    def __init__(self):
        Base.__init__(self, 'mis')

    def info_manage(self):
        self.click_ele(PageElements.main_info_manage_link_text)

    def content_audit(self):
        self.click_ele(PageElements.main_content_audit_link_text)