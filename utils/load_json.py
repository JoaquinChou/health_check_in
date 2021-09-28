import json


def load_json(json_path):
    f = open(json_path, encoding="utf-8").read()
    # 转换为json对象
    param_data = json.loads(f)

    return param_data
