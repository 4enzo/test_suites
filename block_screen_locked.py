# -*- coding: utf-8 -*-
'''
Created on 2019-05-24

@author: Enzo
'''

#定期检测鼠标坐标，如两次坐标相同，则随机移动鼠标
#随机移动鼠标仍存在锁屏问题，改用按win键解决

import time
import random

import pyautogui
pyautogui.FAILSAFE = False
#pyautogui.FAILSAFE = True时 鼠标移动到左上角时会报pyautogui.FailSafeException


while True:
    cur_day = time.strftime('%A', time.localtime())
    hour = time.strftime('%H', time.localtime())
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
	#weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']

    #if cur_day in weekdays and int(hour) in range(0, 24):
    if int(hour) in range(0, 24):
        #获取鼠标位置
        x1, y1 = pyautogui.position()
        sleep_time = 300
        time.sleep(sleep_time)

        x2, y2 = pyautogui.position()

        if x1==x2 and y1==y2:
            #单纯移动鼠标，有时屏幕仍旧会锁屏
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.press('win')
            print(time.strftime('[%Y-%m-%d_%H:%M:%S]:',time.localtime())+'double press key-win')
            #鼠标静止状态下移动到随机位置
            # width, height = pyautogui.size()

            # x = random.randint(0,width)
            # y = random.randint(0,height)
            # pyautogui.moveTo(x=x,y=y,duration=0.5)

        else:
            # print('The mouse position changed in %ds, This time do noting'%sleep_time)
            print(time.strftime('[%Y-%m-%d_%H:%M:%S]:',time.localtime())+'do nothing')
    else:
        print(time.strftime('[%Y-%m-%d_%H:%M:%S]:not working time,sleep 3600s',time.localtime()))
        time.sleep(3600)
