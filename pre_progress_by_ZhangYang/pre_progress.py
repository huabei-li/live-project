import os
import csv
import re
from datetime import datetime

TXT_PATH = 'record.txt'
SAVE_PATH = 'result.txt'
KEY = '我支持调课'
STIME = ''
ETIME = ''


RESULT_LIST = []        # 结果
QQ_OR_EMAIL_LIST = []            # 已存在的QQ


test_string = "2018-08-20 16:45:49 雨勤未晴丶(275922122)"
test_string2 = "#我要换组#、#我要红包#、#我支持调课#管理员开启了全员禁言，只有群主和管理员才能发言"

def get_date(string):
    '''
    以字符串形式返回日期
    :param string: 待查找的字符串
    :return:
    '''
    mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", string)
    if mat:
        return mat.groups()[0]
    return None

def get_time(string):
    '''
    以字符串的形式返回时间
    :param string: 待查找的字符串
    :return:
    '''
    mat = re.search(r"(\d{1,2}:\d{1,2}:\d{1,2})", string)
    if mat:
        return mat.groups()[0]
    return None

def get_nick(string):
    '''
    获得昵称 如果没有出现昵称 返回'无名*'
    :param string: 待查找的字符串
    :return:
    '''
    left_pos = string.find('(')
    if left_pos == -1:
        left_pos = string.find('<')
    if left_pos == 20:
        return '无名*'
    return string[20:left_pos]

def get_qq_or_email(string):
    '''
    获得QQ或者Email
    :param string: 待查找的字符串
    :return:
    '''

    # 查找()中的QQ号
    left_pos = string.find('(')
    right_pos = string.find(')')
    if left_pos != -1:
        return string[left_pos+1:right_pos]

    # 查找<>中的邮箱号
    left_pos = string.find('<')
    right_pos = string.find('>')
    if left_pos != -1:
        return string[left_pos+1:right_pos]



def get_key_list(string):
    '''
    得到以#标记的关键词的列表
    :param string:
    :return:
    '''

    # 关键词列表
    key_list = []

    # 找出字符串中所有‘#’的位置
    jing_pos = []
    for i in range(len(string)):
        if string[i] == '#':
            jing_pos.append(i)

    # '#'号列表长度
    length = len(jing_pos)

    # 用了一个很蠢的方法去跳过
    tmp_flag = 0
    for i in range(length):
        if tmp_flag == 1:
            tmp_flag = 0
            continue
            
        if i+1 == length:
            break

        key = string[jing_pos[i]+1:jing_pos[i+1]]
        key_list.append(key)
        tmp_flag = 1

    return key_list


def pre_process(path, setkey, stime, etime, save_path):
    '''
    预处理函数
    :param path: 聊天记录文本的路径
    :param setkey: 本次活动设置的关键词
    :param stime: 开始时间 以20181010235900的形式传入
    :param etime: 结束时间 以20181010235900的形式传入
    :param save_path: 结果保存的路径
    :return:
    '''
    with open(path, encoding='utf-8') as f:

        # exist为1时表示该QQ or Email已经被标记为参与了抽奖 不再次插入
        exist = 0
        # QQ或者Email
        qq_or_email = None
        # 昵称
        nick = ""

        # 遍历聊天记录中的每一行
        for line in f.readlines():
            # 获取时间和日期
            date = get_date(line)
            time = get_time(line)
            if date and time:
                exist = 0
                qq_or_email = get_qq_or_email(line)
                nick = get_nick(line)
                if qq_or_email in QQ_OR_EMAIL_LIST:
                    exist = 1
            else:
                # 如果已存在 跳过即可
                if exist:
                    continue
                # 获取该行的关键词
                key_list = get_key_list(line)

                # 遍历查找出的每一个关键词
                for key in key_list:
                    if key == setkey:
                        RESULT_LIST.append([qq_or_email, nick, 1])
                        QQ_OR_EMAIL_LIST.append(qq_or_email)
                        exist = 1
                        break

                



if __name__ == "__main__":
    pre_process(TXT_PATH, KEY, 0, 0, 0)
    print('--------------')
    for result in RESULT_LIST:
        print('++++')
        print(result)