import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


class Base:
    def __init__(self, name):
        if name == 'app':
            self.driver = Driver.get_app_driver()
        elif name == 'mp':
            self.driver = Driver.get_mp_driver()
        elif name == 'mis':
            self.driver = Driver.get_mis_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        logging.info('定位单个元素{}'.format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        logging.info('点击')
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=0.5):
        logging.info('输入{}'.format(text))
        input_text = self.search_ele(loc, timeout, poll)
        input_text.clear()
        input_text.send_keys(text)

    def page_exists_text(self, text, type='web'):
        """
        判断某个页面是否存在某个文本
        :param text:检查文本内容
        :param type:平台类型 web  app
        :return:
        """
        text_xpath = None
        if type == 'web':
            text_xpath = (By.XPATH, '//*[contains(text(),"{}")]'.format(text))
        elif type == 'app':
            text_xpath = (By.XPATH, '//*[contains(@text,"{}")]'.format(text))
        try:
            self.search_ele(text_xpath)
            return True
        except TimeoutException:
            return False

    def select_channel(self, channel_btn, channel_list, text):
        """

        :param channel_btn: 选择框按钮
        :param channel_list:选择框文本列表
        :param text:要点击的文本
        :return:
        """
        self.click_ele(channel_btn)
        channel = self.search_eles(channel_list)
        for i in channel:
            if i.text == text:
                i.click()
                break
            ActionChains(self.driver).move_to_element(i).send_keys(Keys.DOWN)  # 光标移动到元素,没找到元素,键盘就按↓按钮
        else:  # 如果遍历了全部都没找到元素，就抛出异常
            raise NoSuchElementException('文本框：{}，没有找到'.format(text))

    def app_swipe_area(self, area_ele, detail_ele, text, tag=1):
        """
        选择某一个区域滑动
        :param area_ele: 滑动区域的元素
        :param detail_ele: 区域里具体的某个元素
        :param text: 定位元素的文本
        :param tag:
        :return:
        """
        # 定位要滑动的区域
        area = self.search_ele(area_ele)

        # 获取宽高
        width = area.size.get('width')
        height = area.size.get('height')

        # 获取左上角的x,y的坐标
        x = area.location.get('x')
        y = area.location.get('y')

        while True:
            # 获取元素结构
            prev_page = self.driver.page_source
            try:  # 异常捕获, 如果点击不到要找的模块就进行滑动
                self.click_ele((detail_ele[0], detail_ele[1].format(text)))
                break
            except TimeoutException:
                if tag == 1:  # 往上滑动
                    self.driver.swipe(x + width * 0.5, y + height * 0.8, x + width * 0.5, y + height * 0.2, 1500)
                if tag == 3:  # 往左滑动
                    self.driver.swipe(x + width * 0.8, y + height * 0.5, x + width * 0.2, y + height * 0.5, 1500)
                if prev_page == self.driver.page_source:  # 滑动之后元素结构不变的话,说明元素找不到,抛出异常
                    raise NoSuchElementException('文本{}没有找到'.format(text))
