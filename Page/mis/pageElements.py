from selenium.webdriver.common.by import By


class PageElements:
    """登录页面"""
    # 账号
    login_account_name = (By.NAME, 'username')
    # 密码
    login_password_name = (By.NAME, 'password')
    # 登录按钮
    login_btn_id = (By.ID, 'inp1')
    """首页"""
    # 信息管理
    main_info_manage_link_text = (By.LINK_TEXT, "信息管理")
    # 内容审核
    main_content_audit_link_text = (By.LINK_TEXT, "内容审核")
    """内容审核"""
    # 文章名称输入框
    audit_search_article_css = (By.CSS_SELECTOR, 'input[placeholder="请输入: 文章名称"]')
    # 结束日期选择按钮
    audit_select_over_btn_css = (By.CSS_SELECTOR, 'input[placeholder="选择结束时间"]')
    # 选择日期
    audit_select_date_btn_xpath = (By.XPATH, "//td[contains(@class,'available')]//span[contains(text(),'{}')]")
    # 日期选择框 确定按钮
    audit_select_date_acc_btn_xpath = (By.XPATH, "//button/span[contains(text(),'确定')]")
    # 查询按钮
    audit_query_article_btn_class = (By.CLASS_NAME, "find")
    # 文章 通过按钮
    audit_article_pass_btn_xpath = (By.XPATH, "//button/span[contains(text(),'通过')]")
    # 审核弹窗 确定按钮
    audit_pass_alert_acc_btn_class = (By.CLASS_NAME, "el-button--primary")
