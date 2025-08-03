import requests

url = "http://10.154.3.9:9000/rmw//datamanage/resmaintain/resMaintainAction!modify.action?objId=-3685003099&resSynflag=null&resClassName=HBO_CID"

payload='HBO_CID__is_wrong=0&HBO_CID__is_wrong=&wrong_info=%2B&HBO_CID__wrong_info=%2B&cid_time=20250722&HBO_CID__cid_time=20250722&HBO_CID__city_id=2013&HBO_CID__city_id=&HBO_CID__county_id=1000139&HBO_CID__county_id=&zh_label=730X31259714&HBO_CID__zh_label=730X31259714&customer_account=730X31259714&HBO_CID__customer_account=730X31259714&cover_type=FTTH&HBO_CID__cover_type=FTTH&HBO_CID__hold_bas_id=-1949942379&HBO_CID__hold_bas_id=&HBO_CID__hold_bas_port_id=-2297483059&HBO_CID__hold_bas_port_id=&HBO_CID__olt_id=-500851134&HBO_CID__olt_id=&HBO_CID__olt_port_id=-2658080466&HBO_CID__olt_port_id=&HBO_CID__hold_onu_id=-3685260185&HBO_CID__hold_onu_id=&HBO_CID__hold_onu_port_id=&HBO_CID__hold_onu_port_id=&svlan_old=1072&HBO_CID__svlan_old=1072&cvlan_old=2106&HBO_CID__cvlan_old=2106&cid_old=trunk%2B63%2F1%2F14%3A1072.2106%2B10.131.38.18%2F1%2F1%2F7%2F0%2F8%2F000000000000CMDCB7A3F909%2BGP&HBO_CID__cid_old=trunk%2B63%2F1%2F14%3A1072.2106%2B10.131.38.18%2F1%2F1%2F7%2F0%2F8%2F000000000000CMDCB7A3F909%2BGP&jx_bas_ip=183.214.159.77&HBO_CID__jx_bas_ip=183.214.159.77&jx_bas_port=trunk%2B63%2F1%2F14&HBO_CID__jx_bas_port=trunk%2B63%2F1%2F14&jx_svlan=1072&HBO_CID__jx_svlan=1072&jx_cvlan=2106&HBO_CID__jx_cvlan=2106&jx_olt_ip=10.131.38.18&HBO_CID__jx_olt_ip=10.131.38.18&jx_olt_pon=1%2F7%2F8&HBO_CID__jx_olt_pon=1%2F7%2F8&jx_onu_sn=CMDCB7A3F909&HBO_CID__jx_onu_sn=CMDCB7A3F909&jx_onu_port=&HBO_CID__jx_onu_port=&jx_onu_type=&HBO_CID__jx_onu_type=&mac=cc%3A96%3Aa2%3A19%3A4e%3A53&HBO_CID__mac=cc%3A96%3Aa2%3A19%3A4e%3A53&HBO_CID__pon_port=-2658080466&HBO_CID__pon_port=&jx_olt_pon2=%E5%B2%B3%E9%98%B3%E5%8E%BF%E9%BA%BB%E5%A1%98%E9%95%87%E4%BC%A0%E8%BE%93%E6%9C%BA%E6%88%BF-OLT001-ZX-C300%2F1-7-GPON-8&HBO_CID__jx_olt_pon2=%E5%B2%B3%E9%98%B3%E5%8E%BF%E9%BA%BB%E5%A1%98%E9%95%87%E4%BC%A0%E8%BE%93%E6%9C%BA%E6%88%BF-OLT001-ZX-C300%2F1-7-GPON-8&lan1=100&HBO_CID__lan1=1000&HBO_CID__is_rate=0&HBO_CID__is_rate=&bras_vendor=%E5%8D%8E%E4%B8%BA&HBO_CID__bras_vendor=%E5%8D%8E%E4%B8%BA&card_type=GTGH&HBO_CID__card_type=GTGH&bandwidth=1000&HBO_CID__bandwidth=1000&HBO_CID__int_id=-3685003099'
headers = {
   'X-IETab': '1',
   'Pragma': 'no-cache',
   'Cookie': 'Cookie=ys-eastSpace=o%3Acollapsed%3Db%253A1; ys-west-panel=o%3Acollapsed%3Db%253A0; JSESSIONID_RMW8000=043F8E2D04505D8B12ED3A7B1CEDA180.group-rmw-8000-221',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept': '*/*',
   'Host': '10.154.3.9:9000',
   'Connection': 'keep-alive',
   'Referer': 'http://10.154.3.9:9000/rmw//datamanage/resmaintain/resMaintainAction!modify.action?objId=-3685003099&resSynflag=null&resClassName=HBO_CID'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)