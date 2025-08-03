import json
import re

import requests

import login_getCookie
from json2payload import  convert_to_payload

cookie = login_getCookie.GetRwmCookie()
print("do.py")
print(cookie)

payheaders = {
   'Pragma': 'no-cache',
   'Cookie': '',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept': '*/*',
   'Host': '10.154.3.9:9000',
   'Connection': 'keep-alive',
   'Referer': 'http://10.154.3.9:9000/rmw//datamanage/resmaintain/resMaintainAction!modify.action?objId=-2372992958&resSynflag=null&resClassName=HBO_CID'
}
payheaders['Cookie'] = cookie.get('Cookie')

def process_file(file_path, process_func):
    """
    读取TXT文件，逐条处理无标记行，完成后标记为1，支持断点续传

    参数：
        file_path: TXT文件路径
        process_func: 处理单条数据的函数（输入原始数据，返回是否成功）
    """
    # 读取所有行并解析状态
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 记录处理进度（行索引：是否需要处理）
    to_process = []
    data_list = []  # 存储原始数据
    for idx, line in enumerate(lines):
        line = line.strip()
        if '|1' in line:
            # 已标记的行：提取原始数据，标记为无需处理
            data = line.split('|')[0]
            to_process.append(False)
        else:
            # 未标记的行：原始数据即为内容，标记为需要处理
            data = line
            to_process.append(True)
        data_list.append(data)

    # 遍历行，处理未标记的数据
    total = len(lines)
    for idx in range(total):
        if not to_process[idx]:
            # 跳过已处理行
            continue

        data = data_list[idx]
        print(f"处理第{idx + 1}/{total}条：{data}")
        try:
            # 执行自定义处理函数（返回True表示成功）
            success = process_func(data)
            if success:
                # 处理成功：标记为|1
                lines[idx] = f"{data}|1\n"
                print(f"第{idx + 1}条处理成功，已标记")
            else:
                print(f"第{idx + 1}条处理失败，不标记")
        except Exception as e:
            print(f"第{idx + 1}条处理出错：{str(e)}，不标记")

        # 实时写入更新（避免程序崩溃丢失标记）
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    print("所有未标记数据处理完毕")


# ------------------------------
# 示例：自定义处理函数（可根据需求替换）
# ------------------------------
def example_process(data):
    """示例处理函数：模拟发送HTTP请求（此处用打印代替）"""
    import time
    try:
        # 模拟处理耗时（如发送请求）

        getJsonValue = requests.request("GET", "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction"
                                           "!preModifyNotag.action?resClassName=HBO_CID&objId="+data,
                                    headers=cookie, data={})
        # 提取数据
        json_data = extract_json_value_data(getJsonValue.text)

        paylod = convert_to_payload(json_data[0])
        url = "http://10.154.3.9:9000/rmw//datamanage/resmaintain/resMaintainAction!modify.action?resSynflag=null&resClassName=HBO_CID?objId="+data

        response = requests.request("POST", url, headers=payheaders, data=paylod)

        print(response.text)
        return True  # 假设处理成功
    except:
        return False

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



if __name__ == "__main__":
    # 假设TXT文件路径为'int_ids.txt'
    # example_process('-2261586819')
    process_file('int_ids.txt',example_process())