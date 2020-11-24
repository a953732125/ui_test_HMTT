from Base.base import Base
from Page.mis.pageElements import PageElements
import datetime,time


class MisAuditPage(Base):
    def __init__(self):
        Base.__init__(self, 'mis')

    def search_article(self, title):
        # 输入文章名称
        self.send_ele(PageElements.audit_search_article_css, title)
        # 点击选择结束日期
        self.click_ele(PageElements.audit_select_over_btn_css)
        time.sleep(2)
        day = datetime.datetime.now().day
        # 选择日期 先对格式化字符串赋值  -> 组装回元组  ->因为 click_ele只支持元组
        self.click_ele((PageElements.audit_select_date_btn_xpath[0]
                        , PageElements.audit_select_date_btn_xpath[1].format(day + 1)))
        # 点击日期的确定按钮
        self.click_ele(PageElements.audit_select_date_acc_btn_xpath)
        # 点击查询
        self.click_ele(PageElements.audit_query_article_btn_class)

    def audit_article(self):
        """审核文章"""
        # 点击文章通过按钮
        self.click_ele(PageElements.audit_article_pass_btn_xpath)
        # 通过按钮的弹窗 点击确认按钮
        self.click_ele(PageElements.audit_pass_alert_acc_btn_class)
