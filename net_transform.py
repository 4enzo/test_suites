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
    #由位数获取掩码，如8————>255.0.0.0
    length = int(input('请输入位数：'))
    res_bin = '1'*length + '0'*(32-length)

    a = int(res_bin[0:8],2)
    b = int(res_bin[8:16],2)
    c = int(res_bin[16:24],2)
    d = int(res_bin[24:32],2)

    r_int = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
    print('\n位数 %d 对应的掩码为：%s\n'%(length,r_int))

def main():
    while True:
        print('*'*20 + '网络转换小工具' + '*'*5 + 'by Enzo' + '*'*20)
        print('1:掩码转位数')
        print('2:位数转掩码')

        print('0:退出')



        fun_num = int(input('请输入编号：'))
        if fun_num == 0:
            break
        elif fun_num == 1:
            mask2length()
            continue
        elif fun_num == 2:
            length2mask()
            continue
        else:
            print('error/功能未实现')



if __name__ == '__main__':
    main()