import time

import requests



# getJsonValue = requests.request("GET", "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction"
#                                            "!preModifyNotag.action?resClassName=HBO_CID&objId=-2345245936",
#                                     headers=get_json_value_data_head, data={})
#
#
# json_data = extract_json_value_data(getJsonValue.text)
# print(json_data)


def GetRwmCookie():
    from get_json_value_data import extract_json_value_data

    url = "http://10.154.3.8:7000/irms/CtrlIrmsLogin.action"

    rmwUrl = "http://10.154.3.9:9000/rmw/index.jsp"

    modifyCidUrl = "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction!modify.action?resSynflag=null&resClassName=HBO_CID&objId="

    loginInfo = 'action=checkLogin&cellphone=Uv5D2FbQsYjY9htQZdxq%2FA%3D%3D&pwd=G2lTAOBF8uPBA4NEXs1iPg%3D%3D&type=1&csrf_token=sFqFL7WOUHzfdN%2FaGU5wMrJTTlRDRI%2FY'
    login_headers = {
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Host': '10.154.3.8:7000',
        'Connection': 'keep-alive'
    }
    # 返回rwm授权
    # login_response = requests.request("POST", url, headers=login_headers, data=loginInfo)
    #
    # print(login_response.headers)
    he = headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': '10.154.3.9:9000',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'foreign=true&token=ZOXgsiXJNTPWnoNLQP%2FVqe8JqpC3maJ6gvZG%2BtlyR0JGmts54TTJhTp7sELB9G20'

    login_response = requests.request("POST", url, headers=login_headers, data=loginInfo)
    #
    print('login_getcookie.py  loginresponse')
    print(login_response.headers)

    tormwurl = "http://10.154.3.8:7000/irms/dataFluxVisitsAction!addAmout.ilf?classify=sysmodel&moduleen=jcgn&modulecn=%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD"

    tooopayload = {}
    toooooheaders = {
        'DNT': '1',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': '',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': '10.154.3.8:7000',
        'Connection': 'keep-alive'
    }
    print("setcooke")
    print(login_response.headers['set-cookie'])
    toooooheaders['Cookie'] = login_response.headers['set-cookie']
    tooooresponse = requests.request("POST", tormwurl, headers=toooooheaders, data=tooopayload)

    he = {
        'DNT': '1',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Host': '10.154.3.9:9000',
        'Connection': 'keep-alive',
        'Cookie': ''
    }

    payload = 'foreign=true&token=ZOXgsiXJNTPWnoNLQP%2FVqe8JqpC3maJ6gvZG%2BtlyR0JGmts54TTJhTp7sELB9G20'
    rwm_response = requests.request("POST", rmwUrl, headers=he, data=payload)
    print('login_getcookie.py  rwmresponse')
    # print(rwm_response.text)
    print(rwm_response.headers)

    get_json_value_data_head = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Accept': '*/*',
        'Host': '10.154.3.9:9000',
        'Connection': 'keep-alive',
        'Cookie': ''
    }
    print(rwm_response.headers['set-cookie'])
    get_json_value_data_head['Cookie'] = rwm_response.headers['set-cookie']

    print(get_json_value_data_head)

    # 返回rwm授权
    return get_json_value_data_head
