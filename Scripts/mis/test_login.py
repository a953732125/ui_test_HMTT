import pytest

from Base.page import Page

from Base.getData import GetData


def get_mis_login_data():
    data_list = []
    data = GetData.get_json_data('publish_audit_article.json')['mis_login']
    data_list.append((data['account'], data['password'], data['exp']))
    return data_list


@pytest.mark.run(order=1)
class TestLogin:
    @pytest.mark.parametrize('account,password,exp', get_mis_login_data())
    def test_login(self, account, password, exp):
        """系统管理员登录"""
        Page.get_mis_login_page().login(account, password)
        assert Page.get_mis_login_page().page_exists_text(exp)
