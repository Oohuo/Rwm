import requests

url = "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction!preModifyNotag.action?resClassName=HBO_CID&objId=-3685003099&date=1753835838649"

payload={}
headers = {
   'Cookie': 'cookie=ys-eastSpace=o%3Acollapsed%3Db%253A1; ys-west-panel=o%3Acollapsed%3Db%253A1; JSESSIONID_RMW8000=5667219AF039A7B0665D698F0A88A944.group-rmw-8000-219; JSESSIONID_RMW8000=EAA7C95FD57C997120B41E0328DE0D26.group-rmw-8000-221',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': '10.154.3.9:9000',
   'Connection': 'keep-alive'
}
import re
import json


def extract_json_value_data(response_text):
    # 使用正则表达式匹配jsonValueData变量的内容
    pattern = r'var jsonValueData = (\[.*?\]);'
    match = re.search(pattern, response_text, re.DOTALL)

    if match:
        # 提取JSON字符串并解析
        json_str = match.group(1)
        try:
            data = json.loads(json_str)
            return data
        except json.JSONDecodeError as e:
            print(f"解析JSON失败: {e}")
            return None
    else:
        print("未找到jsonValueData数据")
        return None


response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
# 提取数据
json_data = extract_json_value_data(response.text)
if json_data:
        print("提取到的jsonValueData数据:")
        print(json_data)