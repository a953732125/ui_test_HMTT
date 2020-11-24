from Page.mp.mpLoginPage import MpLoginPage
from Page.mp.mpHomePage import MpHomePage
from Page.mp.mpPublishArticle import MpPublishArticle
from Page.mis.misLoginPage import MisLoginPage
from Page.mis.misMainPage import MisMainPage
from Page.mis.misAuditPage import MisAuditPage
from Page.app.app_mainPage import AppMainPage


class Page:
    @classmethod
    def get_mp_login(cls):
        return MpLoginPage()

    @classmethod
    def get_mp_home(cls):
        return MpHomePage()

    @classmethod
    def get_mp_publish(cls):
        return MpPublishArticle()

    @classmethod
    def get_mis_login_page(cls):
        return MisLoginPage()

    @classmethod
    def get_mis_main_page(cls):
        return MisMainPage()

    @classmethod
    def get_mis_audit_page(cls):
        return MisAuditPage()

    @classmethod
    def get_app_main(cls):
        return AppMainPage()
