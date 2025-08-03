import requests

from get_json_value_data import extract_json_value_data
from json2payload import json_to_payload

get_json_value_data_head = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': '10.154.3.9:9000',
   'Connection': 'keep-alive',
   'Cookie': ''
}
get_json_value_data_head['Cookie'] = 'JSESSIONID_RMW8000=662F94E915D0C0D48E22467960377F4E.group-rmw-8000-221; Path=/; HttpOnly'
getJsonValue = requests.request("GET", "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction"
                                       "!preModifyNotag.action?resClassName=HBO_CID&objId=-3685003099",
                                headers=get_json_value_data_head, data={},timeout=(2, 2))
json_data = extract_json_value_data(getJsonValue.text)


print(json_data)
data = '-2261586819'



getJsonValue = requests.request("GET", "http://10.154.3.9:9000/rmw/datamanage/resmaintain/resMaintainAction"
                                           "!preModifyNotag.action?resClassName=HBO_CID&objId=" + data,
                                    headers=get_json_value_data_head, data={})

json_data = extract_json_value_data(getJsonValue.text)

# paylod = json_to_payload(json_data[0])
# url = "http://10.154.3.9:9000/rmw//datamanage/resmaintain/resMaintainAction!modify.action?resSynflag=null&resClassName=HBO_CID?objId=" + data
#
# response = requests.request("POST", url, headers=get_json_value_data_head, data=paylod)
#
# print(response.text)
