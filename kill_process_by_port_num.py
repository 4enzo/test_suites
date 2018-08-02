# -*- coding: utf-8 -*-
'''
Created on 2018-08-03

@author: Enzo
'''

'''
工作中开启多个软件有可能会出现端口冲突情况，此脚本找出占用某个端口的进程并kill
环境基于win7 + py3,其他环境未测试
'''

import subprocess

def get_pid(port):
    cmd = 'netstat -ano | findstr "%s"'%port
    cmdstat,results = subprocess.getstatusoutput(cmd)
    if cmdstat == 0:
        find_lable = '0.0.0.0'
        stdout = results.split('\n')
        for item in stdout:
            if find_lable in item:
                ilist = item.strip().split()
                rtit = {}
            #   协议  本地地址          外部地址        状态           PID
                rtit['协议'] = ilist[0]
                rtit['本地地址'] = ilist[1]
                rtit['外部地址'] = ilist[2]
                rtit['状态'] = ilist[3]
                rtit['PID'] = ilist[4]
                print('占用端口%s的进程为%s'%(port,rtit['PID']))
                return rtit['PID']
    elif cmdstat == 1:
        print('未找到占用端口%s的进程'%port)
    else:
        print('执行错误！\n错误信息为：%s' %results)

def kill_pid(pid):
    if pid == None:
        pass
    else:
        cmd = 'taskkill /pid %s -t -f'%pid
        print('开始杀进程%s'%pid)
        cmdstat, results = subprocess.getstatusoutput(cmd)
        if cmdstat == 0:
            print(results)
        else:
            print('杀进程异常:\n%s'%results)


if __name__ == '__main__':

    pid = get_pid('1080')
    kill_pid(pid)
