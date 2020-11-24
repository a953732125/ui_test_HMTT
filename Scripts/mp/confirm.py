from Base.page import Page
import time
from Base.driver import Driver

Page.get_mp_login().login('13911111111', '246810')
print(Page.get_mp_home().get_company_name())
Page.get_mp_home().content_manage()
Page.get_mp_home().publish_article()
Page.get_mp_publish().publish_article('asdasd', 'sdasdsada', 'python')
time.sleep(2)
Driver.quit_mp_driver()
