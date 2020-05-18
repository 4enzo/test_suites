# -*- coding: utf-8 -*-
'''
Created on 2020-05-18

@author: Enzo
'''

import subprocess
import time
import datetime

def start_container():
    cmd = "docker run -d xxxxxx"
    status, container_id = subprocess.getstatusoutput(cmd)
    return container_id

def stop_rm_container(id):
    cmd1 = "docker stop %s" % id
    status1, results = subprocess.getstatusoutput(cmd1)
    cmd2 = "docker rm %s" % id
    status2, results = subprocess.getstatusoutput(cmd2)
    if status1 == 0 and status2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    container_id = start_container()
    while True:
        if datetime.datetime.now().hour == 4:
            stop_rm_container(container_id)
            time.sleep(3600)
            container_id = start_container()
        else:
            time.sleep(600)