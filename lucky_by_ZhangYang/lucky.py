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
    pass