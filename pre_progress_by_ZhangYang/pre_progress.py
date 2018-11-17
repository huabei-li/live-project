import os
import csv
import re
from datetime import datetime
import time

TXT_PATH = 'record.txt'
SAVE_PATH = 'result.txt'
KEY = '我支持调课'
STIME = '20180821000000'
ETIME = '20180831000000'

def get_timestring(string):
    '''
    查找字符串中的时间
    :param string:
    :return:
    '''
    mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})", string)
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


def format_time(timestring):
    '''
    格式化日期字符串 时间字符串 统一为20181010235900的形式
    :param timestring: 时间字符串 形如2018-10-10 23:59:00
    :return: 20181010235900形式的字符串
    '''
    time_struct = time.strptime(timestring, "%Y-%m-%d %H:%M:%S")
    result_string = time.strftime("%Y%m%d%H%M%S", time_struct)
    return result_string


def time_judge(current_time, start_time, end_time):
    '''
    判断当前时间是否在时间段内
    :param current_time: 当前时间
    :param start_time: 时间段开始时间
    :param end_time: 时间段结束时间
    :return: True or False
    '''
    i_current_time = int(current_time)
    i_start_time = int(start_time)
    i_end_time = int(end_time)

    if i_start_time <= i_current_time and i_current_time <= i_end_time:
        return True

    return False


def pre_process(path, setkey, start_time, end_time, save_path):
    '''
    预处理函数
    :param path: 聊天记录文本的路径
    :param setkey: 本次活动设置的关键词
    :param start_time: 开始时间 以20181010235900的形式传入
    :param end_time: 结束时间 以20181010235900的形式传入
    :param save_path: 结果保存的路径
    :return:
    '''

    result_list = []        # 结果
    qq_or_email_list = []  # 已存在的QQ

    with open(path, encoding='utf-8') as f:

        # should_skip为1时表示该QQ or Email已经被标记为参与了抽奖 不再次插入
        should_skip = False
        # QQ或者Email
        qq_or_email = None
        # 昵称
        nick = ""

        # 遍历聊天记录中的每一行
        for line in f.readlines():
            # 获取时间和日期
            timestring = get_timestring(line)
            if timestring:
                formated_time = format_time(timestring)
                if not time_judge(formated_time, start_time, end_time):
                    should_skip = True
                    # print("[-]{}被跳过".format(timestring))
                    continue

                # print("[+]{}被考虑".format(timestring))
                should_skip = False
                qq_or_email = get_qq_or_email(line)
                nick = get_nick(line)
                if qq_or_email in qq_or_email_list:
                    should_skip = True
            else:
                # 如果已存在 跳过即可
                if should_skip:
                    continue
                # 获取该行的关键词
                key_list = get_key_list(line)

                # 遍历查找出的每一个关键词
                for key in key_list:
                    if key == setkey:
                        result_list.append([qq_or_email, nick, 1])
                        qq_or_email_list.append(qq_or_email)
                        should_skip = True
                        break

    # 保存结果
    with open(save_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in result_list:
            writer.writerow(row)
    print('[+]保存成功{}'.format(save_path))


if __name__ == "__main__":
    pre_process(TXT_PATH, KEY, STIME, ETIME, SAVE_PATH)