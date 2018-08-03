# -*- coding: utf-8 -*-
'''
Created on 2018-08-04

@author: Enzo
'''

import subprocess

def ping(ip_start,ip_end):
    ip_list = []
    ip_start_split = ip_start.split('.')
    ip_end_split = ip_end.split('.')

    for i in range(int(ip_start_split[3]),int(ip_end_split[3])+1):
        ip_list.append(ip_start_split[0]+'.'+ip_start_split[1] + '.' + ip_start_split[2] + '.' + str(i))

    for ip in ip_list:
        cmd = 'ping %s'%ip
        cmdstat,results = subprocess.getstatusoutput(cmd)
        if cmdstat == 0:
            if '时间' in results:
                print('%s 正在被使用'%ip)
            else:
                print('%s 没有被使用'%ip)
        else:
            print('Error:',results)

if __name__ == '__main__':
    ip_start = input('请输入开始ip:')
    ip_end = input('请输入结束ip:')
    print('请稍等。。。')
    ping(ip_start,ip_end)
