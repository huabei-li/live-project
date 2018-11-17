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
    mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", string)
    if mat:
        return mat.groups()[0]
    return None

def get_time(string):
    mat = re.search(r"(\d{1,2}:\d{1,2}:\d{1,2})", string)
    if mat:
        return mat.groups()[0]
    return None

def get_nick(string):
    left_pos = string.find('(')
    if left_pos == -1:
        left_pos = string.find('<')
    if left_pos == -1:
        return '无名*'
    return string[20:left_pos]

def get_qq_or_email(string):
    left_pos = string.find('(')
    right_pos = string.find(')')
    if left_pos != -1:
        return string[left_pos+1:right_pos]
    
    left_pos = string.find('<')
    right_pos = string.find('>')
    if left_pos != -1:
        return string[left_pos+1:right_pos]



def get_key_list(string):
    jing_pos = []
    for i in range(len(string)):
        if string[i] == '#':
            jing_pos.append(i)

    key_list = []

    length = len(jing_pos)

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
    with open(path, encoding='utf-8') as f:
        exist = 0
        qq_or_email = None
        nick = ""

        for line in f.readlines():
            date = get_date(line)
            time = get_time(line)
            if date and time:
                exist = 0
                qq_or_email = get_qq_or_email(line)
                nick = get_nick(line)
                if qq_or_email in QQ_OR_EMAIL_LIST:
                    exist = 1
            else:
                if exist:
                    continue
                key_list = get_key_list(line)
                for key in key_list:
                    if key == setkey:
                        RESULT_LIST.append([qq_or_email, nick, 1])
                        print(qq_or_email)
                        print(nick)
                        print(line)
                        QQ_OR_EMAIL_LIST.append(qq_or_email)
                        exist = 1
                        break

                



if __name__ == "__main__":
    pre_process(TXT_PATH, KEY, 0, 0, 0)
    print('--------------')
    for result in RESULT_LIST:
        print('++++')
        print(result)