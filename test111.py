import requests
from urllib.parse import urlparse, parse_qs, urlunparse
import re


def update_ctr_v2(classify, moduleen, modulecn, url, name):
    """模拟updateCTRV2函数的功能"""
    # 构建请求URL
    base_url = "/irms/dataFluxVisitsAction!addAmout.ilf"
    params = {
        "classify": classify,
        "moduleen": moduleen,
        "modulecn": modulecn
    }

    try:
        # 发送POST请求
        response = requests.post(
            f"http://10.154.3.9:9000{base_url}",  # 需要替换为实际域名
            params=params,
            allow_redirects=False
        )

        # 检查请求结果
        if response.text.strip() == '':
            # 成功且响应为空，打开新窗口
            open_new_win(url, name)
        else:
            # 响应非空，执行登出
            logout()
    except Exception as e:
        print(f"请求失败: {e}")
        # 请求失败，执行登出
        logout()


def open_new_win(url, name):
    """模拟openNewWin函数的功能"""
    if url in ('#', ''):
        return None

    # 检查是否为外部系统URL
    other_sys = '://' in url

    # 解析URL
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # 处理特定情况
    if not other_sys and parsed_url.query:
        # 非外部系统且有查询参数，添加msg=old
        query_params['msg'] = ['old']

    # 处理特定IP和用户的情况（这里仅作判断，不修改URL）
    if '10.154.3.10:7000' in url:
        user_account = query_params.get('useraccount', [])
        if any(ua in ['jt', 'root'] for ua in user_account):
            print("检测到特定IP和用户组合")

    # 准备表单数据
    form_data = {}

    # 处理不同模块的特殊参数
    if name == "oslgis" and 'useraccount' in query_params:
        form_data['useraccount'] = "ZOXgsiXJNTPWnoNLQP/Vqbum0Ngi7QcLjAeSKWmpFBq4fRppGkY8VU1iFyNV9Oqv"
    elif (name in ["jcgnby", "jcgn"]) and 'useraccount' in query_params:
        form_data['token'] = "ZOXgsiXJNTPWnoNLQP/Vqbum0Ngi7QcLjAeSKWmpFBq4fRppGkY8VU1iFyNV9Oqv"
    elif 'token' in query_params:
        form_data['token'] = "ZOXgsiXJNTPWnoNLQP/Vqbum0Ngi7QcLjAeSKWmpFBq4fRppGkY8VU1iFyNV9Oqv"
    else:
        # 添加所有查询参数
        for key, values in query_params.items():
            form_data[key] = values[0]  # 只取第一个值

    # 如果没有查询参数，添加默认useraccount
    if not query_params:
        form_data['useraccount'] = "ZOXgsiXJNTPWnoNLQP/Vqbum0Ngi7QcLjAeSKWmpFBq4fRppGkY8VU1iFyNV9Oqv"

    # 构建提交URL（去掉查询参数部分）
    submit_url = urlunparse(parsed_url._replace(query=''))

    print(f"准备提交到: {submit_url}")
    print(f"表单数据: {form_data}")

    try:
        # 发送POST请求模拟表单提交
        response = requests.post(submit_url, data=form_data, allow_redirects=True)
        print(f"提交成功，状态码: {response.status_code}")
        # 这里可以根据需要处理响应内容
        return response
    except Exception as e:
        print(f"提交失败: {e}")
        return None


def logout():
    """模拟登出操作"""
    try:
        # 发送登出请求
        response = requests.get("http://10.154.3.9:9000/jsp/logout.jsp")  # 需要替换为实际域名
        print("登出请求已发送")
        # 重定向到/irms
        print("重定向到 /irms")
        # 实际应用中可以在这里处理重定向
    except Exception as e:
        print(f"登出失败: {e}")
        # 无论成功失败都重定向
        print("重定向到 /irms")


# 执行示例
if __name__ == "__main__":
    update_ctr_v2(
        'sysmodel',
        'jcgn',
        '基础功能',
        'http://10.154.3.9:9000/rmw/index.jsp?foreign=true&useraccount=uy_zouhan',
        'jcgn'
    )
