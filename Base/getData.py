import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class GetData:
    @classmethod
    def get_json_data(cls, file_name):
        with open('./Data' + os.sep + file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
