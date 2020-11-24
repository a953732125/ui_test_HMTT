from Base.base import Base
from Page.mp.pageElements import PageElements


class MpLoginPage(Base):
    def __init__(self):
        Base.__init__(self, 'mp')

    def login(self, phone, code):
        # 输入手机号
        self.send_ele(PageElements.login_phone_css, phone)
        # 输入验证码
        self.send_ele(PageElements.login_code_css, code)
        # 点击登录按钮
        self.click_ele(PageElements.login_btn_xpath)
