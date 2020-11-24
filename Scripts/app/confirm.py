import time
from Base.driver import Driver
from Base.page import Page

Page.get_app_main().select_banner_channel('go')
time.sleep(2)
Driver.quit_app_driver()