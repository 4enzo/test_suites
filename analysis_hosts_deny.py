# -*- coding: utf-8 -*-
'''
Created on 2019-08-19

@author: Enzo
'''

import time
import json
import requests
import logging

import pymongo


#vps天天被爆破，故安装DenyHosts,当某个ip尝试登陆三次失败后，将此ip加入hosts.deny，以屏蔽该ip
#前期hosts.deny以肉眼可见的速度增加，目前已拉黑1w余个ip,正好利用一下这些ip分析一下攻击分布区域

#尝试使用http://ip.taobao.com/查询ip归属地，发现限制严重，暂时转到http://ip-api.com/json/{query}
#接口说明参考http://ip-api.com/docs/api:json


def get_hosts_deny():
    hosts_list = []
    file_hosts_deny = './hosts.deny'
    with open(file_hosts_deny) as f:
        for line in f.readlines():
            if "ALL: " == line[:5]:
                hosts_list.append(line[5:].replace("\n",""))
                # print("The deny host is %s"%line[5:])
        return hosts_list

def get_hosts_location(ip):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    # url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + ip
    url = "http://ip-api.com/json/" + ip + "?lang=zh-CN"
    try:
        result = requests.get(url,headers=headers)
        if result.status_code == 200:
            content = json.loads(result.text)
            if content["status"] == "success":
                # print(content)
                return content
        else:
            print("error:result.status_code:%s"%result.status_code)

    except Exception as e:
        print("error:"+ip)

def write2file(location):
    with open('./location.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(location)+'\n')

def load_file():
    location_list = []
    with open('./location.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            location_list.append(json.loads(line))
            # print(json.loads(line))

    return location_list

def find_db(ip):
    ip_flag = False
    conn = pymongo.MongoClient('192.168.123.100', 27017)
    db = conn.mydata
    my_collection = db.hosts_deny
    if my_collection.find_one({"query": ip}):
        ip_flag = True
    else:
        pass
    conn.close()
    return ip_flag

def write2db(location_info):

    conn = pymongo.MongoClient('192.168.123.100',27017)
    # 连接mydata数据库，没有则自动创建
    db = conn.mydata
    # 使用hosts_deny集合，没有则自动创建
    my_collection = db.hosts_deny
    # if my_collection.find_one({"query":location_info["query"]}):
    #     pass
    # else:
    #     my_collection.insert(location_info)
    #     print("插入数据库")
    my_collection.insert(location_info)

    conn.close()


def main():
    for ip in get_hosts_deny():
        if find_db(ip):
            pass
        else:
            a = get_hosts_location(ip)
            write2db(get_hosts_location(ip))
            time.sleep(1)
    #     write2file(a)
    # for line in load_file():
        # print(line)
    # for line in load_file():
    #     print(line)



if __name__ == '__main__':
    main()