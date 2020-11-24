import time

import pytest
from Base.page import Page
from Base.getData import GetData


def get_audit_data():
    data_list = []
    data = GetData.get_json_data('publish_audit_article.json')['mis_audit_article']
    data_list.append((data['title'], data['exp']))
    return data_list


@pytest.mark.run(order=2)
class TestAudit:
    def setup_class(self):
        Page.get_mis_main_page().info_manage()
        Page.get_mis_main_page().content_audit()

    @pytest.mark.parametrize('audit_title,exp', get_audit_data())
    def test_audit(self, audit_title, exp):
        Page.get_mis_audit_page().search_article(audit_title)
        time.sleep(2)
        Page.get_mis_audit_page().audit_aricle()
        assert Page.get_mis_audit_page().page_exists_text(exp)
