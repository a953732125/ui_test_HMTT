import time

from Base.page import Page
from Base.driver import Driver

Page.get_mis_login_page().login('testid', 'testpwd123')
Page.get_mis_main_page().info_manage()
Page.get_mis_main_page().content_audit()
time.sleep(2)
Page.get_mis_audit_page().search_article('审核文章xxx')
Page.get_mis_audit_page().audit_aricle()
time.sleep(2)
Driver.quit_mis_driver()
