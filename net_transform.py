# -*- coding: utf-8 -*-
'''
Created on 2019-03-28

@author: Enzo
'''


def mask2length():
    #由掩码xxx.xxx.xxx.xxx得到掩码长度，如255.0.0.0————>8
    mask = input('请输入掩码（xxx.xxx.xxx.xxx）:')
    r_bin = ''
    for i in mask.split('.'):
        r_bin += bin(int(i))[2:]

    print('\n掩码 %s 对应的长度为：%d\n'%(mask,len(r_bin.replace('0',''))))

def length2mask():
    pass

def main():
    while True:
        print('*'*20 + '网络转换小工具' + '*'*5 + 'by Enzo' + '*'*20)
        print('1:掩码转位数')
        print('2:位数转掩码（未实现）')

        print('0:退出')



        fun_num = int(input('请输入编号：'))
        if fun_num == 0:
            break
        elif fun_num == 1:
            mask2length()
            continue
        else:
            print('error/功能未实现')



if __name__ == '__main__':
    main()