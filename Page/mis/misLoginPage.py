from Base.base import Base
from Page.mis.pageElements import PageElements


class MisLoginPage(Base):
    def __init__(self):
        Base.__init__(self, 'mis')

    def login(self, name, pwd):
        # 输入账号密码
        self.send_ele(PageElements.login_account_name, name)
        self.send_ele(PageElements.login_password_name, pwd)
        # 删除登录按钮的disabled属性
        js = 'document.getElementById("inp1").removeAttribute("disabled");'
        self.driver.execute_script(js)
        # 点击登录
        self.click_ele(PageElements.login_btn_id)
