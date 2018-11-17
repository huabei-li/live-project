import os
import numpy as np
import random
import csv


def get_lucky_boys(infos, prize_count_list):
    '''
    获取中奖人名单(只能获得一次奖)
    :param infos: 本次抽奖参与者信息（qq or email, nick, weight）
    :param prize_count_list: 奖品数量组成的列表 按照重要等级序
                             如一等奖1个 二等奖2个 三等奖3个可以传入[1,2,3]
                             如只有一个一等奖 可以传入[1]
                             支持任意数量（也别太多）
    :return: 如果prize_count传入[1,2,3]则返回[[info_1_1], [info_2_1, info_2_2], [info_3_1, info_3_2, info_3_3]]
             以此类推 其中info为（qq or email, nick, weight）
    '''
    # 结果
    result = []
    # 总的奖品数量
    total_count = sum(prize_count_list)
    # 总权重
    total_weight = 0
    # 总用户数
    total_user = len(infos)
    # 赢者表
    win_user_id_list = []

    # 区间的左右端点
    left_pos = np.zeros((total_user), dtype=int)
    right_pos = np.zeros((total_user), dtype=int)
    # 是否已经被抽中过
    won_flag = np.zeros((total_user), dtype=int)

    # 对于每个用户 维护用户掌管的区间的左右端点
    for i in range(total_user):
        left_pos[i] = total_weight
        total_weight += infos[i][2]
        right_pos[i] = total_weight - 1

    # 共进行total_count(奖品的数量)轮
    for count in range(total_count):
        # 直到得到获奖者为止
        get_winner = False
        while not get_winner:
            r_int = random.randint(0, total_weight - 1)
            # 遍历参与者寻找随机的数字落在哪个区间
            for i in range(total_user):
                if left_pos[i] <= r_int and r_int <= right_pos[i] and won_flag[i] == 0:
                    get_winner = True
                    win_user_id_list.append(i)
                    won_flag[i] = 1
                    break

    # 根据胜者表得到各个奖项的获奖者
    pos = 0
    for prize_count in prize_count_list:
        tmp_info_list = []
        for i in range(prize_count):
            tmp_info_list.append(infos[win_user_id_list[pos]])
            pos += 1
        result.append(tmp_info_list)

    for infos in result:
        for info in infos:
            print(info)
        print('--------------------')

    return result


info_path = "result.txt"

with open(info_path, encoding='utf-8') as f:
    infos = []
    reader = csv.reader(f)
    for info in reader:
        info[2] = int(info[2])
        infos.append(info)

get_lucky_boys(infos, [3, 2, 3])
