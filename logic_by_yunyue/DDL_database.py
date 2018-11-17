#insert 活动表（常规）
def insert_act(act_id, act_name, key, w_a, sta, pt, start_t, end_T, show_T ):
    import sqlite3
    conn = sqlite3.connect('alpha.sqlite')

    c = conn.cursor()

    c.execute("""INSERT INTO Activity VALUES (?,?,?,?,?,?,?,?,?)""", (act_id, act_name, key, w_a, sta, pt, start_t, end_T, show_T))

    conn.commit()
    conn.close() 


#insert_user（常规）
def insert_user(id,nk,num,wei):
    import sqlite3
    conn = sqlite3.connect('alpha.sqlite')

    c = conn.cursor()
    c.execute("""INSERT INTO user VALUES (?,?,?,?)""", (id, nk, num, wei))
        
    conn.commit()
    conn.close()

#插入获奖表（标准）
def insert_win(ac_id, u_id, rank):
    import sqlite3
    if ac_id and u_id:
        con = sqlite3.connect('alpha.sqlite')
        c = con.cursor()
        c.execute('insert into win values (?,?,?)', (ac_id, u_id, rank))
        con.commit()
        con.close()

#用状态筛选活动表，返回所有的信息
'''
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3]
'''
def select_activity(status):
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute('select * from Activity where status = ?', (status,))

    activity_list = []
    for item in cursor:
        activity_list.append(item)
    con.close()

    return activity_list


    #con.close()



#查询获奖表，参数为活动ID（ac_id）返回所有用户
'''
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3]
'''
def select_win(ac_id):
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute('select ac_name, keyword, rank, nickname, win.u_id from Activity, user, win where ? = Activity.ac_id and Activity.ac_id = win.ac_id and user.u_id = win.u_id and user.ac_id = Activity.ac_id order by rank asc',(ac_id))

    activity_list = []
    for item in cursor:
        activity_list.append(item)
    con.close()

    return activity_list

#根据活动状态返回消息,已创建
def select_status1():
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute("select ac_name, keyword, wenan, start_time, end_time, show_time from Activity where status=1")
    activity_list = []
    for item in cursor:
        activity_list.append(item)
    con.close()

    return activity_list


#根据活动状态返回消息,已发布
def select_status2():
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute("select ac_name, keyword, wenan, start_time, end_time, show_time from Activity where status=2")
    activity_list = []
    for item in cursor:
        activity_list.append(item)
    con.close()

    return activity_list


#根据活动状态返回消息,已开奖
def select_status3():
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute("select ac_name, keyword, wenan, start_time, end_time, show_time from Activity where status=3")
    activity_list = []
    for item in cursor:
        activity_list.append(item)
    con.close()

    return activity_list



#删除某活动，传入活动id（活动插入时间）
def delete_activity(ac_id):
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    c.execute('delete from Activity where ac_id = ? ', (ac_id,))
    con.commit()
    con.close()


def raw_exec(string):
    '''
    执行SQL指令 返回相关结果
    :param string:
    :return:
    '''
    import sqlite3
    con = sqlite3.connect('alpha.sqlite')
    c = con.cursor()
    cursor = c.execute(string)

    result_list = []
    for item in cursor:
        result_list.append(item)
    con.close()

    return result_list