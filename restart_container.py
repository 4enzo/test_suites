# -*- coding: utf-8 -*-
'''
Created on 2020-05-18

@author: Enzo
'''

import subprocess
import time
import datetime

def start_container(container_name):
    cmd = "docker run -d -p 443:443 --name %s --restart=always xxxxxx"%container_name
    status, result = subprocess.getstatusoutput(cmd)
    if status == 0:
        return True
    else:
        print("Error:%s"%result)
        return False

def stop_rm_container(container_name):
    cmd = "docker stop %s && docker rm %s" % (container_name,container_name)
    status, result = subprocess.getstatusoutput(cmd)
    if status == 0:
        return True
    else:
        print("Error:%s"%result)
        return False

if __name__ == '__main__':
    container_name = "container_name"
    if start_container(container_name):
        while True:
            if datetime.datetime.now().hour == 4:
                stop_rm_container(container_name)
                time.sleep(3600)
                start_container(container_name)
            else:
                time.sleep(600)