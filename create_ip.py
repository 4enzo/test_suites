# -*- coding: utf-8 -*-
'''
Created on 2020-04-09

@author: Enzo
'''

import random
import time

def create_ip_24mask():
    #生成大量不同网段的随机ip(24位掩码)。排除组播地址及127本地地址
    start_time = time.time()
    ip_list = []
    i = 1
    with open(".\\random_ip_24mask.txt",'a') as f:
        while i <= 300000:
            a = random.randint(1,220)
            b = random.randint(1,255)
            c = random.randint(1,255)
            # d = random.randint(1,255)
            tmp_ip = "%d.%d.%d.1"%(a,b,c)
            if a != 127:
                if tmp_ip not in ip_list:
                    ip_list.append(tmp_ip)
                    f.write(tmp_ip+'\n')
                    i+=1
                else:
                    pass
            else:
                pass

    end_time = time.time()
    print("time spend %ss"%(end_time-start_time))

if __name__ == '__main__':
    create_ip_24mask()
