from selenium.webdriver.common.by import By


class PageElements:
    # banner滑动框
    main_banner_area_class = (By.CLASS_NAME, 'android.widget.HorizontalScrollView')
    # banner选择渠道
    main_banner_select_channel_xpath = (By.XPATH, '//android.widget.HorizontalScrollView//*[contains(@text,"{}")]')
