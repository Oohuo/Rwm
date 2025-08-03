import urllib.parse
import get_translate


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

def json_to_payload(json_data):
    """
    将JSON数据转换为符合要求的payload字符串

    参数:
        json_data: 包含原始数据的字典（从JSON解析而来）

    返回:
        符合格式的application/x-www-form-urlencoded字符串
    """
    # 构建参数键值对列表（保持原始payload的参数顺序和格式）
    params = []

    # 1. 固定参数（非JSON映射的固定值）
    params.append(('HBO_CID__is_wrong', '0'))
    params.append(('HBO_CID__is_wrong', ''))  # 重复键，空值
    params.append(('wrong_info', '+'))
    params.append(('HBO_CID__wrong_info', '+'))
    params.append(('cid_time', json_data.get('cid_time', '')))  # 与HBO_CID__cid_time值相同
    params.append(('HBO_CID__city_id','2013'))
    params.append(('HBO_CID__city_id',''))
    params.append(('HBO_CID__county_id','1000139'))
    params.append(('HBO_CID__county_id',''))
    params.append(('hold_bas_id', json_data.get('hold_bas_id', '')))
    params.append(('hold_bas_id', ''))
    params.append(('hold_bas_port_id', json_data.get('hold_bas_port_id', '')))
    params.append(('hold_bas_port_id',''))
    params.append(('olt_id', json_data.get('olt_id', '')))
    params.append(('olt_id',''))
    params.append(('olt_port_id', json_data.get('olt_port_id', '')))
    params.append(('olt_port_id',''))
    params.append(('HBO_CID__hold_onu_id', json_data.get('HBO_CID__hold_onu_id', '')))
    params.append(('HBO_CID__hold_onu_id',''))
    params.append(('HBO_CID__lan1','1000'))
    params.append(('HBO_CID__bandwidth',''))



    # 2. JSON映射参数（按原始payload顺序排列）
    mapping = [
        # (JSON键, payload键, 是否需要URL编码)
        ('cid_time', 'HBO_CID__cid_time', False),
        ('zh_label', 'zh_label', False),
        ('zh_label', 'HBO_CID__zh_label', False),
        ('customer_account', 'customer_account', False),
        ('customer_account', 'HBO_CID__customer_account', False),
        ('cover_type', 'cover_type', False),
        ('cover_type', 'HBO_CID__cover_type', False),
        ('hold_onu_id', 'HBO_CID__hold_onu_id', False),
        ('hold_onu_id', 'HBO_CID__hold_onu_id', False),  # 重复键，空值
        ('hold_onu_port_id', 'HBO_CID__hold_onu_port_id', False),
        ('hold_onu_port_id', 'HBO_CID__hold_onu_port_id', False),  # 重复键，空值
        ('svlan_old', 'svlan_old', False),
        ('svlan_old', 'HBO_CID__svlan_old', False),
        ('cvlan_old', 'cvlan_old', False),
        ('cvlan_old', 'HBO_CID__cvlan_old', False),
        ('cid_old', 'cid_old', True),  # 需要URL编码（原始payload中已编码）
        ('cid_old', 'HBO_CID__cid_old', True),  # 需要URL编码
        ('jx_bas_ip', 'jx_bas_ip', False),
        ('jx_bas_ip', 'HBO_CID__jx_bas_ip', False),
        ('jx_bas_port', 'jx_bas_port', True),  # 包含特殊字符，需编码
        ('jx_bas_port', 'HBO_CID__jx_bas_port', True),
        ('jx_svlan', 'jx_svlan', False),
        ('jx_svlan', 'HBO_CID__jx_svlan', False),
        ('jx_cvlan', 'jx_cvlan', False),
        ('jx_cvlan', 'HBO_CID__jx_cvlan', False),
        ('jx_olt_ip', 'jx_olt_ip', False),
        ('jx_olt_ip', 'HBO_CID__jx_olt_ip', False),
        ('jx_olt_pon', 'jx_olt_pon', True),  # 包含特殊字符，需编码
        ('jx_olt_pon', 'HBO_CID__jx_olt_pon', True),
        ('jx_onu_sn', 'jx_onu_sn', False),
        ('jx_onu_sn', 'HBO_CID__jx_onu_sn', False),
        ('jx_onu_port', 'jx_onu_port', False),
        ('jx_onu_port', 'HBO_CID__jx_onu_port', False),
        ('jx_onu_type', 'jx_onu_type', False),
        ('jx_onu_type', 'HBO_CID__jx_onu_type', False),
        ('mac', 'mac', True),  # 包含冒号，需编码
        ('mac', 'HBO_CID__mac', True),
        ('pon_port', 'HBO_CID__pon_port', False),
        ('jx_olt_pon2', 'jx_olt_pon2', True),  # 包含特殊字符，需编码
        ('jx_olt_pon2', 'HBO_CID__jx_olt_pon2', True),
        ('lan1', 'lan1', False),
        ('is_rate', 'HBO_CID__is_rate', False),
        ('is_rate', 'HBO_CID__is_rate', False),  # 重复键，空值
        ('bras_vendor', 'bras_vendor', True),
        ('bras_vendor', 'HBO_CID__bras_vendor', True),
        ('card_type', 'card_type', False),
        ('card_type', 'HBO_CID__card_type', False),
        ('bandwidth', 'bandwidth', False),
        ('int_id', 'HBO_CID__int_id', False),
    ]

    # 处理映射参数（只编码需要编码的字段，且仅编码一次）
    for json_key, payload_key, need_encode in mapping:
        # 获取值并处理空值
        value = json_data.get(json_key, '')
        if value is None:
            value = ''
        str_value = str(value)

        # 仅对标记为需要编码的字段执行一次URL编码
        if need_encode:
            # 第一次编码（仅一次）
            str_value = urllib.parse.quote(str_value)

        params.append((payload_key, str_value))

    # 3. 转换为最终格式（关键：禁用自动编码，因为我们已经手动编码过了）
    # 使用quote_via=lambda x, *_: x 告诉urlencode不要对值进行编码
    print(params)
    return urllib.parse.urlencode(params, doseq=True, quote_via=lambda x, *_: x)


# # get_translate.query_maintain_info()
# # 测试示例
# if __name__ == "__main__":
#     # 原始JSON数据
#     json_data = {'bras_vendor': '华为', 'cid_old': 'trunk+63/1/14:1072.2106+10.131.38.18/1/1/7/0/8/000000000000CMDCB7A3F909+GP', 'olt_port_id': '岳阳县麻塘镇传输机房-OLT001-ZX-C300/1-7-GPON-8', 'stateflag': 0, 'pon_port': '岳阳县麻塘镇传输机房-OLT001-ZX-C300/1-7-GPON-8', 'lan1': '100', 'cvlan_old': '2106', 'mac': 'cc:96:a2:19:4e:53', 'is_rate': '是', 'hold_onu_port_id': '', 'jx_onu_port': '', 'county_id': '岳阳县', 'svlan_old': '1072', 'jx_onu_sn': 'CMDCB7A3F909', 'jx_onu_type': '', 'jx_bas_ip': '183.214.159.77', 'int_id': '-3685003099', 'wrong_info': '+', 'customer_account': '730X31259714', 'time_stamp': '2025-07-25 09:40:01', 'jx_olt_ip': '10.131.38.18', 'bandwidth': '1000', 'hold_bas_id': 'HNYUY-MB-CMNET-BRAS21-ME60YYX', 'card_type': 'GTGH', 'jx_olt_pon': '1/7/8', 'cover_type': 'FTTH', 'zh_label': '730X31259714', 'hold_bas_port_id': 'GE1/0/1(10G)', 'olt_id': '岳阳县麻塘镇传输机房-OLT001-ZX-C300', 'jx_svlan': '1072', 'jx_olt_pon2': '岳阳县麻塘镇传输机房-OLT001-ZX-C300/1-7-GPON-8', 'cid_time': '20250722', 'hold_onu_id': '岳阳/岳阳县麻塘镇传输机房ZD-ONU0001-KZ-HG51e-730X31259714', 'jx_cvlan': '2106', 'jx_bas_port': 'trunk+63/1/14', 'is_wrong': '是', 'city_id': '岳阳'}
#     valuejson = {'bras_vendor': '华为', 'cid_old': 'trunk 63/1/87:1028.2020 10.131.37.168/1/1/3/0/7/000000000000ZTEGCB75205C GP', 'olt_port_id': -3256470206, 'stateflag': 0, 'pon_port': -3256470206, 'lan1': '100', 'cvlan_old': '2020', 'mac': '44:fb:5a:73:61:0e', 'is_rate': 0, 'hold_onu_port_id': None, 'jx_onu_port': None, 'county_id': 1000139, 'svlan_old': '1028', 'jx_onu_sn': 'ZTEGCB75205C', 'jx_onu_type': None, 'jx_bas_ip': '183.214.159.77', 'int_id': -2345245936, 'wrong_info': ' ', 'customer_account': '730X13694206', 'time_stamp': '2025-07-31 05:26:50', 'jx_olt_ip': '10.131.37.168', 'bandwidth': '300', 'hold_bas_id': None, 'card_type': 'GFBT', 'jx_olt_pon': '1/3/7', 'cover_type': 'FTTH', 'zh_label': '730X13694206', 'hold_bas_port_id': None, 'olt_id': -3253847407, 'jx_svlan': '1028', 'jx_olt_pon2': '岳阳县城南无线机房-OLT001-ZX-C600/1-3-GPON_XGPON-7', 'cid_time': '20250722', 'hold_onu_id': -3257981164, 'jx_cvlan': '2020', 'jx_bas_port': 'trunk 63/1/87', 'is_wrong': 0, 'city_id': 2013}
#     # 生成payload
#     payload = json_to_payload(valuejson)
#     print(payload)

def convert_to_payload(data):
    # 严格定义参数处理顺序及规则：
    # 每个配置项包含：参数名、是否生成普通键、前缀键处理方式、编码方式
    param_configs = [
        # 1. is_wrong：仅前缀键，带值+空值
        {"param": "is_wrong", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 2. wrong_info：普通键+前缀键，均为+（空格编码为+）
        {"param": "wrong_info", "has_normal": True, "prefix_modes": ["value"], "encode": "plus"},
        # 3. cid_time：普通键+前缀键，均为值
        {"param": "cid_time", "has_normal": True, "prefix_modes": ["value"]},
        # 4. city_id：仅前缀键，带值+空值
        {"param": "city_id", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 5. county_id：仅前缀键，带值+空值
        {"param": "county_id", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 6. zh_label：普通键+前缀键，均为值
        {"param": "zh_label", "has_normal": True, "prefix_modes": ["value"]},
        # 7. customer_account：普通键+前缀键，均为值
        {"param": "customer_account", "has_normal": True, "prefix_modes": ["value"]},
        # 8. cover_type：普通键+前缀键，均为值
        {"param": "cover_type", "has_normal": True, "prefix_modes": ["value"]},
        # 9. hold_bas_id：仅前缀键，均为空值
        {"param": "hold_bas_id", "has_normal": False, "prefix_modes": ["empty", "empty"]},
        # 10. hold_bas_port_id：仅前缀键，均为空值
        {"param": "hold_bas_port_id", "has_normal": False, "prefix_modes": ["empty", "empty"]},
        # 11. olt_id：仅前缀键，带值+空值
        {"param": "olt_id", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 12. olt_port_id：仅前缀键，带值+空值
        {"param": "olt_port_id", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 13. hold_onu_id：仅前缀键，带值+空值
        {"param": "hold_onu_id", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 14. hold_onu_port_id：仅前缀键，均为空值
        {"param": "hold_onu_port_id", "has_normal": False, "prefix_modes": ["empty", "empty"]},
        # 15. svlan_old：普通键+前缀键，均为值
        {"param": "svlan_old", "has_normal": True, "prefix_modes": ["value"]},
        # 16. cvlan_old：普通键+前缀键，均为值
        {"param": "cvlan_old", "has_normal": True, "prefix_modes": ["value"]},
        # 17. cid_old：普通键+前缀键，空格编码为+
        {"param": "cid_old", "has_normal": True, "prefix_modes": ["value"], "encode": "plus"},
        # 18. jx_bas_ip：普通键+前缀键，均为值
        {"param": "jx_bas_ip", "has_normal": True, "prefix_modes": ["value"]},
        # 19. jx_bas_port：普通键+前缀键，空格编码为+
        {"param": "jx_bas_port", "has_normal": True, "prefix_modes": ["value"], "encode": "plus"},
        # 20. jx_svlan：普通键+前缀键，均为值
        {"param": "jx_svlan", "has_normal": True, "prefix_modes": ["value"]},
        # 21. jx_cvlan：普通键+前缀键，均为值
        {"param": "jx_cvlan", "has_normal": True, "prefix_modes": ["value"]},
        # 22. jx_olt_ip：普通键+前缀键，均为值
        {"param": "jx_olt_ip", "has_normal": True, "prefix_modes": ["value"]},
        # 23. jx_olt_pon：普通键+前缀键，均为值
        {"param": "jx_olt_pon", "has_normal": True, "prefix_modes": ["value"]},
        # 24. jx_onu_sn：普通键+前缀键，均为值
        {"param": "jx_onu_sn", "has_normal": True, "prefix_modes": ["value"]},
        # 25. jx_onu_port：普通键+前缀键，均为空值
        {"param": "jx_onu_port", "has_normal": True, "prefix_modes": ["empty"]},
        # 26. jx_onu_type：普通键+前缀键，均为空值
        {"param": "jx_onu_type", "has_normal": True, "prefix_modes": ["empty"]},
        # 27. mac：普通键+前缀键，均为值
        {"param": "mac", "has_normal": True, "prefix_modes": ["value"]},
        # 28. pon_port：仅前缀键，带值+空值
        {"param": "pon_port", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 29. jx_olt_pon2：普通键+前缀键，均为值
        {"param": "jx_olt_pon2", "has_normal": True, "prefix_modes": ["value"]},
        # 30. lan1：普通键+前缀键，均为值
        {"param": "lan1", "has_normal": True, "prefix_modes": ["value"]},
        # 31. is_rate：仅前缀键，带值+空值
        {"param": "is_rate", "has_normal": False, "prefix_modes": ["value", "empty"]},
        # 32. bras_vendor：普通键+前缀键，均为值
        {"param": "bras_vendor", "has_normal": True, "prefix_modes": ["value"]},
        # 33. card_type：普通键+前缀键，均为值
        {"param": "card_type", "has_normal": True, "prefix_modes": ["value"]},
        # 34. bandwidth：普通键+前缀键，均为值
        {"param": "bandwidth", "has_normal": True, "prefix_modes": ["value"]},
        # 35. int_id：仅前缀键，带值
        {"param": "int_id", "has_normal": False, "prefix_modes": ["value"]},
    ]

    payload_parts = []
    for config in param_configs:
        param = config["param"]
        # 获取原始值并处理None为空白
        raw_value = data.get(param, None)
        str_value = str(raw_value) if raw_value is not None else ""

        # 选择编码方式（空格编码为+或%20）
        if config.get("encode") == "plus":
            encoded = urllib.parse.quote_plus(str_value)
        else:
            encoded = urllib.parse.quote(str_value)

        # 处理普通键（若需要）
        if config["has_normal"]:
            # 普通键值：根据前缀模式取编码值或空
            normal_value = encoded if config["prefix_modes"][0] == "value" else ""
            payload_parts.append(f"{param}={normal_value}")

        # 处理前缀键（HBO_CID__xxx）
        for mode in config["prefix_modes"]:
            prefix_key = f"HBO_CID__{param}"
            # 特殊处理：HBO_CID__lan1和HBO_CID__bandwidth固定为1000
            if (param == "lan1" or param == "bandwidth") and prefix_key in [f"HBO_CID__lan1", f"HBO_CID__bandwidth"]:
                prefix_value = "1000"  # 固定值
            else:
                prefix_value = encoded if mode == "value" else ""
            payload_parts.append(f"{prefix_key}={prefix_value}")

    return "&".join(payload_parts)
# 测试代码
if __name__ == "__main__":
    # 原始数据
    valuejson = {
            "bras_vendor": "华为",
            "cid_old": "trunk 63/1/89:1029.2040 10.131.37.167/1/1/6/0/8/000000000000NBELFA85C4E9 GP",
            "olt_port_id": -3310411818,
            "stateflag": 0,
            "pon_port": -3310411818,
            "lan1": "100",
            "cvlan_old": "2040",
            "mac": "08:47:d0:cb:6a:2b",
            "is_rate": 0,
            "hold_onu_port_id": None,
            "jx_onu_port": None,
            "county_id": 1000139,
            "svlan_old": "1029",
            "jx_onu_sn": "NBELFA85C4E9",
            "jx_onu_type": None,
            "jx_bas_ip": "211.142.208.213",
            "int_id": -2261586819,
            "wrong_info": " ",
            "customer_account": "730X11958304",
            "time_stamp": "2025-08-01 03:44:50",
            "jx_olt_ip": "10.131.37.167",
            "bandwidth": "300",
            "hold_bas_id": None,
            "card_type": "GFBT",
            "jx_olt_pon": "1/6/8",
            "cover_type": "FTTH",
            "zh_label": "730X11958304",
            "hold_bas_port_id": None,
            "olt_id": -3254491480,
            "jx_svlan": "1029",
            "jx_olt_pon2": "岳阳县311C-RAN数据机房-OLT001-ZX-C600/1-6-GPON_XGPON-8",
            "cid_time": "20250731",
            "hold_onu_id": -3311716448,
            "jx_cvlan": "2040",
            "jx_bas_port": "trunk 63/1/89",
            "is_wrong": 0,
            "city_id": 2013
        }

    # 转换为payload
    payload = convert_to_payload(valuejson)
    print(payload)
