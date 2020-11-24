# import time
#
# from selenium import webdriver
#
#
# class Driver:
#     __driver = None
#
#     @classmethod
#     def get_driver(cls):
#         if cls.__driver is None:
#             cls.__driver = webdriver.Edge()
#             cls.__driver.get('https://www.baidu.com')
#         return cls.__driver
#
#     @classmethod
#     def quit_driver(cls):
#         if cls.__driver:
#             cls.__driver.close()
#             cls.__driver = None
#
#
# if __name__ == '__main__':
#     d = Driver.get_driver()
#     time.sleep(2)
#     Driver.quit_driver()
