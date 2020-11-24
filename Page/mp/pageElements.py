from selenium.webdriver.common.by import By


class PageElements:
    """登录"""
    # 手机号
    login_phone_css = (By.CSS_SELECTOR, 'input[placeholder="请输入手机号"]')
    # 验证码
    login_code_css = (By.CSS_SELECTOR, 'input[placeholder="验证码"]')
    # 登录按钮
    login_btn_xpath = (By.XPATH, "//button/span[text()='登录']")
    """首页"""
    # 公司名字
    home_company_name_class = (By.CLASS_NAME, "company-container")
    # 内容管理
    home_content_manage_xpath = (By.XPATH, "//div[@class='el-submenu__title']/span[text()='内容管理']")
    # 发布文章
    home_publish_article_xpath = (By.XPATH, "//li[contains(@class,'el-menu-item') and contains(text(),'发布文章')]")
    # 用户名
    home_username_class = (By.CLASS_NAME, 'user-name')

    """发表文章"""
    # 文章标题
    publish_article_title_css = (By.CSS_SELECTOR, 'input[placeholder="文章名称"]')
    # frame
    publish_article_frame = "publishTinymce_ifr"
    # 内容
    publish_article_content_id = (By.ID, "tinymce")
    # 封面
    publish_article_fm_xpath = (By.XPATH, "//span[contains(text(),'无图')]")
    # 请选择
    publish_article_select_css = (By.CSS_SELECTOR, 'input[placeholder="请选择"]')
    # 频道
    publish_article_channel_list_xpath = (By.CSS_SELECTOR, "li.el-select-dropdown__item span")
    # 发表按钮
    publish_article_btn_xpath = (By.XPATH, "//button/span[text()='发表']")
