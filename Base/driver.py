from selenium import webdriver as web_dri
from appium import webdriver as app_dri


class Driver:
    __app_driver = None
    __mis_driver = None
    __mp_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.itcast.toutiaoApp',
                'appActivity': '.MainActivity',
                'automationName': 'uiautomator2',
                'noReset': True
            }
            cls.__app_driver = app_dri.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            return cls.__app_driver
        else:
            return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None

    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = web_dri.Edge()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.get('http://ttmis.research.itcast.cn/')
            return cls.__mis_driver
        else:
            return cls.__mis_driver

    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver:
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = web_dri.Edge()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.get('http://ttmp.research.itcast.cn/')
            return cls.__mp_driver
        else:
            return cls.__mp_driver

    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver:
            cls.__mp_driver.quit()
            cls.__mp_driver = None
