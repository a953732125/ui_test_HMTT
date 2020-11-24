from Base.base import Base
from Base.page import Page
import pytest
from Base.getData import GetData


def get_publish_article_data():
    data_list = []
    data = GetData.get_json_data('publish_audit_article.json')['mp_publish_article']
    data_list.append((data['title'], data['content'], data['channel'], data['exp']))
    return data_list


@pytest.mark.run(order=2)
class TestPublishArticle:
    def setup_class(self):
        Page.get_mp_home().content_manage()
        Page.get_mp_home().publish_article()

    @pytest.mark.parametrize('title,content,channel,exp', get_publish_article_data())
    def test_publish_article(self, title, content, channel, exp):
        Page.get_mp_publish().publish_article(title, content, channel)
        assert Page.get_mp_publish().page_exists_text(exp)
