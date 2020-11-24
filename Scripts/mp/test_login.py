import pytest
from Base.page import Page
from Base.getData import GetData


def get_mp_login_data():
    data_list = []
    data = GetData.get_json_data('publish_audit_article.json')['mp_login']
    data_list.append((data['phone'], data['code'], data['exp']))
    return data_list


@pytest.mark.run(order=1)
class TestLogin:
    @pytest.mark.parametrize('phone,code,exp', get_mp_login_data())
    def test_login(self, phone, code, exp):
        Page.get_mp_login().login(phone, code)
        assert Page.get_mp_login().page_exists_text(exp)

    # def teardown_class(self):
    #     Driver.quit_mp_driver()
