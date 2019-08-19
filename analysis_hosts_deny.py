# -*- coding: utf-8 -*-
'''
Created on 2019-08-19

@author: Enzo
'''

import json
import requests


#vps天天被爆破，故安装DenyHosts,当某个ip尝试登陆三次失败后，将此ip加入hosts.deny，以屏蔽该ip
#前期hosts.deny以肉眼可见的速度增加，目前已拉黑1w余个ip,正好利用一下这些ip分析一下攻击分布区域

#尝试使用http://ip.taobao.com/查询ip归属地，发现限制严重，暂时转到http://ip-api.com/json/{query}
#接口说明参考http://ip-api.com/docs/api:json


def get_hosts_deny():
    file_hosts_deny = '.\hosts.deny'
    with open(file_hosts_deny) as f:
        for line in f.readlines():
            if "ALL: " == line[:5]:
                print("The deny host is %s"%line[5:])


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
}


def get_hosts_locaion(ip):
    # url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + ip
    url = "http://ip-api.com/json/" + ip + "?lang=zh-CN"
    result = requests.get(url,headers=headers)
    if result.status_code == 200:
        content = json.loads(result.text)
        if content["status"] == "success":
            print(content)
            return content
    else:
        print("error:result.status_code:%s"%result.status_code)


if __name__ == '__main__':
    # get_hosts_deny()
    get_hosts_locaion("1.2.3.4")