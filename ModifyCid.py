import http.client
import json
import urllib.parse
import time


def load_json_data(file_path):
    """从JSON文件加载数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"错误：文件 {file_path} 不是有效的JSON格式")
        return None
    except Exception as e:
        print(f"加载JSON文件时出错：{str(e)}")
        return None


def build_payload(data):
    """根据JSON数据构建请求payload"""
    # 构建基础payload映射关系，JSON字段 -> 请求参数
    payload_mapping = {
        "bras_vendor": "HBO_CID__bras_vendor",
        "cid_old": "HBO_CID__cid_old",
        "olt_port_id": "HBO_CID__olt_port_id",
        "pon_port": "HBO_CID__pon_port",
        "lan1": "HBO_CID__lan1",
        "cvlan_old": "HBO_CID__cvlan_old",
        "mac": "HBO_CID__mac",
        "is_rate": "HBO_CID__is_rate",
        "hold_onu_port_id": "HBO_CID__hold_onu_port_id",
        "jx_onu_port": "HBO_CID__jx_onu_port",
        "county_id": "HBO_CID__county_id",
        "svlan_old": "HBO_CID__svlan_old",
        "jx_onu_sn": "HBO_CID__jx_onu_sn",
        "jx_onu_type": "HBO_CID__jx_onu_type",
        "jx_bas_ip": "HBO_CID__jx_bas_ip",
        "int_id": "HBO_CID__int_id",
        "wrong_info": "HBO_CID__wrong_info",
        "customer_account": "HBO_CID__customer_account",
        "jx_olt_ip": "HBO_CID__jx_olt_ip",
        "bandwidth": "HBO_CID__bandwidth",
        "hold_bas_id": "HBO_CID__hold_bas_id",
        "card_type": "HBO_CID__card_type",
        "jx_olt_pon": "HBO_CID__jx_olt_pon",
        "cover_type": "HBO_CID__cover_type",
        "zh_label": "HBO_CID__zh_label",
        "hold_bas_port_id": "HBO_CID__hold_bas_port_id",
        "olt_id": "HBO_CID__olt_id",
        "jx_svlan": "HBO_CID__jx_svlan",
        "jx_olt_pon2": "HBO_CID__jx_olt_pon2",
        "cid_time": "HBO_CID__cid_time",
        "hold_onu_id": "HBO_CID__hold_onu_id",
        "jx_cvlan": "HBO_CID__jx_cvlan",
        "jx_bas_port": "HBO_CID__jx_bas_port",
        "is_wrong": "HBO_CID__is_wrong",
        "city_id": "HBO_CID__city_id"
    }

    # 添加原始payload中需要保留的其他字段
    payload = {
        "HBO_CID__is_wrong=0": "",
        # 可以根据需要添加其他固定字段
    }

    # 处理JSON数据并添加到payload
    for json_key, payload_key in payload_mapping.items():
        if json_key in data:
            value = data[json_key] if data[json_key] is not None else ""
            # 特殊处理需要URL编码的字段
            if json_key in ["cid_old"]:
                payload[payload_key] = urllib.parse.quote(str(value))
            else:
                payload[payload_key] = str(value)

    # 转换为application/x-www-form-urlencoded格式
    return urllib.parse.urlencode(payload)


def send_request(host, port, path, payload, headers):
    """发送HTTP POST请求"""
    try:
        conn = http.client.HTTPSConnection(host, port)
        conn.request("POST", path, payload, headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        return res.status, data.decode("utf-8")
    except Exception as e:
        return None, f"请求发送失败：{str(e)}"


def main(json_file_path):
    # 加载JSON数据
    json_data = load_json_data(json_file_path)
    if not json_data:
        return

    # 服务器配置
    host = "10.154.3.9"
    port = 9000
    path = "/rmw//datamanage/resmaintain/resMaintainAction!modify.action?objId=-2345245936&resSynflag=null&resClassName=HBO_CID"

    # 请求头配置
    headers = {
        'X-IETab': '1',
        'Pragma': 'no-cache',
        'Cookie': 'Cookie=ys-eastSpace=o%3Acollapsed%3Db%253A1; ys-west-panel=o%3Acollapsed%3Db%253A0; JSESSIONID_RMW8000=043F8E2D04505D8B12ED3A7B1CEDA180.group-rmw-8000-221',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Host': f'{host}:{port}',
        'Connection': 'keep-alive',
        'Referer': f'http://{host}:{port}/rmw//datamanage/resmaintain/resMaintainAction!modify.action?objId=-2345245936&resSynflag=null&resClassName=HBO_CID'
    }

    # 如果JSON数据是列表则循环处理每个条目，否则处理单个条目
    if isinstance(json_data, list):
        items = json_data
    else:
        items = [json_data]

    # 循环发送请求
    for i, item in enumerate(items, 1):
        print(f"\n处理第 {i} 条数据...")

        # 构建payload
        payload = build_payload(item)
        if not payload:
            print("构建payload失败，跳过该条目")
            continue

        # 发送请求
        status, response = send_request(host, port, path, payload, headers)

        # 处理响应
        if status is not None:
            print(f"请求发送成功，状态码: {status}")
            print(f"响应内容: {response[:500]}...")  # 只显示前500个字符
        else:
            print(f"请求发送失败: {response}")

        # 避免请求过于频繁
        time.sleep(1)


if __name__ == "__main__":
    # 替换为你的JSON文件路径
    json_file = "data.json"
    main(json_file)
