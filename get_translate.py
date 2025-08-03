import requests
import json


def query_maintain_info(attributeenname, condition, parse_json=True):
    """
    根据attributeenname和condition参数查询接口信息，兼容非标准JSON响应

    参数:
        attributeenname: 要查询的属性名，如'city_id'、'county_id'等
        condition: 查询条件，如'id:2013'
        parse_json: 是否尝试解析为JSON，默认为True

    返回:
        如果parse_json为True且解析成功，返回解析后的字典
        如果parse_json为True但解析失败，返回原始文本并打印警告
        如果parse_json为False，直接返回原始响应文本
    """
    # 构建URL
    url = f"http://10.154.3.9:9000/rmw/datamanage/querymaintain/getSelectValue.action?seldataexpset=1&attributeenname={attributeenname}&cndtype=0"

    # 构建请求体
    payload = f'condition={requests.utils.quote(condition)}&resclass=HBO_CID'

    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Pragma': 'no-cache',
        'Cookie': 'Cookie= ys-eastSpace=o%3Acollapsed%3Db%253A1; ys-west-panel=o%3Acollapsed%3Db%253A0; JSESSIONID_RMW8000=DA6DB5720B7B54C1A7EBA44A3024D49B.group-rmw-8000-222; JSESSIONID_RMW8000=3BF2D83D668EC80D52538882F244F925.group-rmw-8000-220',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Host': '10.154.3.9:9000',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()  # 检查HTTP错误状态码
        raw_response = response.text

        if not parse_json:
            return raw_response

        # 尝试修复可能的非标准JSON（如没有引号的键）
        try:
            # 尝试直接解析
            return json.loads(raw_response)
        except json.JSONDecodeError:
            # 尝试修复常见的非标准格式问题
            import re
            # 给没有引号的键添加双引号
            fixed_json = re.sub(r'(\w+)\s*:', r'"\1":', raw_response)
            # 处理单引号
            fixed_json = fixed_json.replace("'", '"')
            try:
                return json.loads(fixed_json)
            except json.JSONDecodeError as e:
                print(f"警告: 无法解析响应为JSON，返回原始文本。错误: {e}")
                return raw_response

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
        return None


# 使用示例
if __name__ == "__main__":
    # 查询并尝试解析JSON（默认行为）
    result = query_maintain_info('hold_bas_id', 'id:-1949942379')
    print(result)

    # 如果解析有问题，可以选择不解析，直接获取原始文本
    # raw_result = query_maintain_info('city_id', 'id:2013', parse_json=False)
    # print("原始响应文本:")
    # print(raw_result)
